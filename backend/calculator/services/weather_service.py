# SPDX-License-Identifier: AGPL-3.0-or-later
import datetime
from django.core.cache import cache
from django.db.models import Model
from django.utils import timezone
from twisted.conch.client import default

from calculator.models import (
    CurrentTariffModel,
    SolarForecastRecordModel,
    WeatherDataModel,
    DataEntryLineModel,
    SystemEventModel,
)
from calculator.services.PanelPowerCalculationService import PanelPowerCalculationService


class WeatherForecastService:
    def _get_error_response(self, tariff):
        return {
            "predicted_total_kwh": 0.0, "predicted_savings": 0.0, "hourly_forecast_wh": [0.0] * 24,
            "currency": "UAH", "peak_hour": 0, "status": "error", "tariff_used": tariff,
            "current_temp": 0.0, "weather_condition": "Unavailable", "weather_code": 0, "calibration_factor": 1.0
        }

    def _calculate_calibration_factor(self):
        today = datetime.date.today()
        start_date = datetime.date(today.year, today.month, 1)
        yesterday = today - datetime.timedelta(days=1)
        if yesterday < start_date:
            return 1.0

        actual_qs = DataEntryLineModel.objects.filter(date__range=(start_date, yesterday))
        forecast_qs = SolarForecastRecordModel.objects.filter(date__range=(start_date, yesterday))

        actual_dict = {q.date.day: float(q.full_day_power)
                       for q in actual_qs
                       if q.full_day_power is not None and q.full_day_power > 0}

        forecast_dict = {q.date.day: float(q.predicted_kwh)
                         for q in forecast_qs
                         if q.predicted_kwh is not None}

        total_real = 0.0
        total_pred = 0.0

        for day, real_power in actual_dict.items():
            if day in forecast_dict:
                total_real = sum(actual_dict.values()) / 1000.0
                total_pred = sum(forecast_dict.values())

        return (total_real / total_pred) if total_pred > 0 else 1.0
        # return 1.0

    def get_solar_forecast(self, data, user, current_tariff=None):
        if not data or 'hourly' not in data:
            return self._get_error_response(current_tariff)

        api_lat, api_lon = round(data.get('latitude', 0.0), 2), round(data.get('longitude', 0.0), 2)
        cache_key = f'solar_forecast_{api_lat}_{api_lon}'
        if (cached := cache.get(cache_key)): return cached

        if current_tariff is None:
            current_tariff = CurrentTariffModel.load().power_tariff

        radiation_data = data.get('hourly', {}).get('shortwave_radiation', [])
        if not radiation_data: return self._get_error_response(current_tariff)

        surface_pressure = data.get('hourly', {}).get('surface_pressure', [])

        try:
            calibration_factor = self._calculate_calibration_factor()
            print(f"DEBUG: Calibration Factor: {calibration_factor}")

            calc_service = PanelPowerCalculationService()
            total_hourly_wh, detailed_reports = calc_service.get_total_forecast(
                radiation_data, calibration_factor, user
            )

            weather_h = data.get('hourly', {})
            wmo_codes = {0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast", 45: "Fog",
                         95: "Thunderstorm"}

            current_hour = datetime.datetime.now().hour
            safe_h = min(current_hour, len(weather_h.get('temperature_2m', [])) - 1)

            temp = weather_h.get('temperature_2m', [0])[safe_h]
            code = weather_h.get('weather_code', [0])[safe_h]
            wind_dir = weather_h.get('wind_direction_10m', [0])[safe_h]

            result_dict = {
                "predicted_total_kwh": round(sum(total_hourly_wh) / 1000, 2),
                "predicted_savings": round((sum(total_hourly_wh) / 1000) * current_tariff, 2),
                "hourly_forecast_wh": [round(h, 2) for h in total_hourly_wh],
                "detailed_arrays": detailed_reports,
                "status": "success",
                "current_temp": round(temp, 1),
                "weather_condition": wmo_codes.get(code, "Unknown"),
                "weather_code": code,
                "calibration_factor": round(calibration_factor, 2),
                "peak_hour": total_hourly_wh.index(max(total_hourly_wh)) if total_hourly_wh else 0,
                "wind_direction": wind_dir,
            }

            cache.set(cache_key, result_dict, 3600)
            self.save_forecast_to_db(result_dict, data)
            self.check_and_log_wind_alert(data)
            return result_dict
        except Exception as e:
            print(f"WeatherService Error: {e}")
            return self._get_error_response(current_tariff)

    def convert_iso_to_datetime(self, data):
        sunrise_str = data.get('daily', {}).get('sunrise', [''])[0]
        sunset_str = data.get('daily', {}).get('sunset', [''])[0]

        sunrise = datetime.datetime.fromisoformat(sunrise_str)
        sunset = datetime.datetime.fromisoformat(sunset_str)

        return timezone.make_aware(sunrise), timezone.make_aware(sunset)

    def save_forecast_to_db(self, forecast_data, raw_api_data):
        try:
            today = timezone.localtime(timezone.now()).date()
            sunrise_dt, sunset_dt = self.convert_iso_to_datetime(raw_api_data)

            hourly_raw = raw_api_data.get('hourly', {})
            wind_speeds = hourly_raw.get('wind_speed_10m', [])
            wind_gusts = hourly_raw.get('wind_gusts_10m', [])
            wind_directions = hourly_raw.get('wind_direction_10m', [])

            avg_speed = round(sum(wind_speeds) / len(wind_speeds), 1) if wind_speeds else None
            max_gust = max(wind_gusts) if wind_gusts else None
            avg_direction = int(sum(wind_directions) / len(wind_directions)) if wind_directions else None

            SolarForecastRecordModel.objects.update_or_create(
                date=today,
                defaults={
                    'predicted_kwh': forecast_data.get('predicted_total_kwh', 0.0),
                    'predicted_savings': forecast_data.get('predicted_savings', 0.0),
                    'peak_hour': forecast_data.get('peak_hour', 0),
                    'sunrise': sunrise_dt,
                    'sunset': sunset_dt,
                    'wind_speed_10m': avg_speed,
                    'wind_gusts_10m': max_gust,
                    'wind_direction_10m': avg_direction,
                }
            )

            hourly = raw_api_data.get('hourly', {})
            timestamps = hourly.get('time', [])
            if not timestamps:
                return True

            temps = hourly.get('temperature_2m', [])
            codes = hourly.get('weather_code', [])
            clouds = hourly.get('cloud_cover', [])
            humidities = hourly.get('relative_humidity_2m', [])
            surface_pressure = hourly.get('surface_pressure', [])
            shortwave = hourly.get('shortwave_radiation', [])
            direct = hourly.get('direct_radiation', [])
            diffuse = hourly.get('diffuse_radiation', [])

            parsed_timestamps = []
            for ts in timestamps:
                naive_dt = datetime.datetime.strptime(ts, '%Y-%m-%dT%H:%M')
                parsed_timestamps.append(timezone.make_aware(naive_dt))

            WeatherDataModel.objects.filter(timestamp__in=parsed_timestamps).delete()

            weather_objects = []
            for i in range(len(timestamps)):
                def get_val(arr, idx):
                    return arr[idx] if idx < len(arr) else None

                weather_objects.append(
                    WeatherDataModel(
                        timestamp=parsed_timestamps[i],
                        temperature=get_val(temps, i),
                        condition_code=str(get_val(codes, i)) if get_val(codes, i) is not None else "0",
                        cloud_cover=get_val(clouds, i),
                        humidity=get_val(humidities, i),
                        surface_pressure=get_val(surface_pressure, i),
                        shortwave_radiation=get_val(shortwave, i) or 0.0,
                        direct_radiation=get_val(direct, i) or 0.0,
                        diffuse_radiation=get_val(diffuse, i) or 0.0,
                    )
                )

            WeatherDataModel.objects.bulk_create(weather_objects)
            return True

        except Exception as e:
            print(f"DB loading error: {e}")
            return False

    def check_and_log_wind_alert(self, raw_api_data):
        threshold = 15.0

        hourly_raw = raw_api_data.get('hourly', {})
        wind_speeds = hourly_raw.get('wind_speed_10m', [])
        gust_speeds = hourly_raw.get('wind_gusts_10m', [])
        wind_direction = hourly_raw.get('wind_direction_10m', [])
        timestamps = hourly_raw.get('time', [])

        for i in range(len(wind_speeds)):
            max_wind = wind_speeds[i]
            max_gust = gust_speeds[i]

            dt = datetime.datetime.fromisoformat(timestamps[i])
            aware_dt = timezone.make_aware(dt)

            if max_wind >= threshold or max_gust >= threshold:
                time_str = timestamps[i]

                # today = timezone.localtime().date()
                if not SystemEventModel.objects.filter(
                        category='WARNING',
                        message__contains=time_str
                ):
                    event_data = {
                        'wind': max_wind,
                        'gust': max_gust,
                        'direction': wind_direction[i] if i < len(wind_direction) else None,
                        'status': 'CRITICAL' if (max_wind >= threshold and max_gust >= threshold) else 'WARNING'
                    }

                    SystemEventModel.objects.update_or_create(
                        category='WARNING',
                        event_timestamp=aware_dt,
                        defaults={
                            'level': 'WARN',
                            'title': f'Wind alert at {dt.strftime("%H:%M")}',
                            'payload': event_data,
                            'message': f"Recorded at {time_str}: Wind {max_wind} m/s, Gust {max_gust} m/s, Direction {wind_direction}"
                        }
                    )