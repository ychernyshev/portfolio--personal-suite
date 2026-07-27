# SPDX-License-Identifier: AGPL-3.0-or-later
import datetime

from django.core.cache import cache
from django.utils import timezone

from calculator.models import (
    CurrentTariffModel,
    SolarForecastRecordModel,
    WeatherDataModel,
    DataEntryLineModel,
    SystemEventModel,
    PeakEventModel, WindEventModel,
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
            self.check_and_log_wind_alert(data, user=user)

            self.check_and_log_peak_events(data, result_dict.get('peak_hour'), user=user)

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

    # CELERY
    def _fetch_raw_weather_from_api(self, lat, lon):
        import requests
        url = (
            f"https://api.open-meteo.com/v1/forecast"
            f"?latitude={lat}&longitude={lon}"
            f"&hourly=temperature_2m,relative_humidity_2m,surface_pressure,cloud_cover,"
            f"shortwave_radiation,direct_radiation,diffuse_radiation,wind_speed_10m,"
            f"wind_gusts_10m,wind_direction_10m,weather_code"
            f"&daily=sunrise,sunset&timezone=auto"
        )
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(f"Weather API Fetch Error: {e}")
        return None

    def update_forecast_for_user(self, user):
        try:
            settings = getattr(user, 'settings', None)
            if not settings or settings.latitude is None or settings.longitude is None:
                return False

            raw_data = self._fetch_raw_weather_from_api(settings.latitude, settings.longitude)
            if not raw_data:
                return False

            self.get_solar_forecast(raw_data, user)
            return True

        except Exception as e:
            print(f"Error updating forecast for user {user.username}: {e}")
            return False

    # END

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

    def check_and_log_wind_alert(self, raw_api_data, user=None):
        if not user:
            print("DEBUG WIND: User not transferred, skipping wind alerts.")
            return

        threshold = 15.0

        hourly_raw = raw_api_data.get('hourly', {})
        wind_speeds = hourly_raw.get('wind_speed_10m', [])
        wind_gusts = hourly_raw.get('wind_gusts_10m', [])
        wind_direction = hourly_raw.get('wind_direction_10m', [])
        timestamps = hourly_raw.get('time', [])

        today = timezone.localtime(timezone.now()).date()

        daily_event, _ = SystemEventModel.objects.update_or_create(
            date=today,
            user=user,
            defaults={
                "payload": {
                    "title": "Wind alert",
                    "message": "Strong wind detected",
                    "level": "warning",
                    "category": "warning",
                    "max_wind_speed": max(wind_speeds) if wind_speeds else None,
                    "max_wind_gust": max(wind_gusts) if wind_gusts else None,
                }
            }
        )

        for i in range(len(wind_speeds)):
            dt = datetime.datetime.fromisoformat(timestamps[i])
            aware_dt = timezone.make_aware(dt)

            if aware_dt.date() != today:
                continue

            max_wind = wind_speeds[i]
            max_gust = wind_gusts[i]

            if max_wind >= threshold or max_gust >= threshold:
                time_str = timestamps[i]
                title_str = f'Wind alert at {dt.strftime("%H:%M")}'

                if not WindEventModel.objects.filter(
                        daily_event=daily_event,
                        title__icontains=time_str
                ).exists():
                    event_data = {
                        'wind': max_wind,
                        'gust': max_gust,
                        'direction': wind_direction[i] if i < len(wind_direction) else None,
                        'status': 'CRITICAL' if (max_wind >= threshold and max_gust >= threshold) else 'WARNING'
                    }

                    WindEventModel.objects.update_or_create(
                        daily_event=daily_event,
                        user=user,
                        event_timestamp=aware_dt,
                        defaults={
                            'category': 'WARNING',
                            'title': title_str,
                            'message': f"Recorded at {time_str}: Wind {max_wind} m/s, Gust {max_gust} m/s, Direction {wind_direction}",
                            'is_persistent': True,
                            'user': user
                        }
                    )

    def check_and_log_peak_events(self, raw_api_data, peak_hour, user=None):
        if not user:
            print("DEBUG PEAK: User not transferred, skipping peak generation hours.")
            return

        if peak_hour is None:
            print("DEBUG PEAK: peak_hour is None")
            return

        hourly_raw = raw_api_data.get('hourly', {})
        timestamps = hourly_raw.get('time', [])
        if not timestamps or peak_hour >= len(timestamps):
            print("DEBUG PEAK: Invalid timestamps or peak_hour index out of range")
            return

        today = timezone.localtime(timezone.now()).date()

        daily_event, _ = SystemEventModel.objects.update_or_create(
            date=today,
            user=user,
            defaults={
                "payload": {
                    "title": "Wind alert",
                    "message": "Strong wind detected",
                    "level": "warning",
                    "category": "warning",
                }
            }
        )

        peak_start_str = timestamps[peak_hour]
        peak_start_dt = datetime.datetime.strptime(peak_start_str, '%Y-%m-%dT%H:%M')
        peak_start_aware = timezone.make_aware(peak_start_dt)

        end_index = peak_hour + 1
        peak_end_aware = None
        if end_index < len(timestamps):
            peak_end_dt = datetime.datetime.strptime(timestamps[end_index], '%Y-%m-%dT%H:%M')
            peak_end_aware = timezone.make_aware(peak_end_dt)

        PeakEventModel.objects.get_or_create(
            daily_event=daily_event,
            user=user,
            peak_hour=peak_hour,
            status='PEAK_START',
            defaults={
                'created_at': timezone.now()
            }
        )
        print(f"DEBUG PEAK: Created/Checked PeakEvent START for {peak_start_dt.strftime('%H:%M')}")

        if peak_end_aware and peak_end_aware.date() == today:
            PeakEventModel.objects.get_or_create(
                daily_event=daily_event,
                user=user,
                peak_hour=peak_hour,
                status='PEAK_END',
                defaults={
                    'created_at': timezone.now()
                }
            )
            print(f"DEBUG PEAK: Created/Checked PeakEvent END for {peak_end_dt.strftime('%H:%M')}")

    # def check_and_log_peak_events(self, raw_api_data, peak_hour, user=None):
    #     if peak_hour is None:
    #         return
    #
    #     hourly_raw = raw_api_data.get('hourly', {})
    #     timestamps = hourly_raw.get('time', [])
    #     if not timestamps or peak_hour >= len(timestamps):
    #         return
    #
    #     now = timezone.localtime(timezone.now())
    #
    #     peak_start_dt = datetime.datetime.fromisoformat(timestamps[peak_hour])
    #     peak_start_aware = timezone.make_aware(peak_start_dt)
    #
    #     end_index = peak_hour + 1
    #     if end_index < len(timestamps):
    #         peak_end_dt = datetime.datetime.fromisoformat(timestamps[end_index])
    #         peak_end_aware = timezone.make_aware(peak_end_dt)
    #     else:
    #         peak_end_aware = None
    #
    #     base_filter = {'category': 'FORECAST'}
    #     if user:
    #         base_filter['user'] = user
    #
    #     if now.hour >= peak_start_dt.hour:
    #         if not SystemEventModel.objects.filter(
    #                 **base_filter,
    #                 event_timestamp=peak_start_aware,
    #                 title__icontains='Peak generation started'
    #         ).exists():
    #             SystemEventModel.objects.update_or_create(
    #                 **base_filter,
    #                 event_timestamp=peak_start_aware,
    #                 defaults={
    #                     'level': 'SUCC',
    #                     'title': f'Peak generation started at {peak_start_dt.strftime("%H:%M")} ☀️',
    #                     'payload': {'peak_hour': peak_hour, 'status': 'PEAK_START'},
    #                     'is_persistent': True,
    #                     'user': user
    #                 }
    #             )
    #
    #     if peak_end_aware and now.hour >= peak_end_dt.hour:
    #         if not SystemEventModel.objects.filter(
    #                 **base_filter,
    #                 event_timestamp=peak_end_aware,
    #                 title__icontains='Peak generation ended'
    #         ).exists():
    #             SystemEventModel.objects.update_or_create(
    #                 **base_filter,
    #                 event_timestamp=peak_end_aware,
    #                 defaults={
    #                     'level': 'INFO',
    #                     'title': f'Peak generation ended at {peak_end_dt.strftime("%H:%M")} ⛅',
    #                     'payload': {'peak_hour': peak_hour, 'status': 'PEAK_END'},
    #                     'is_persistent': True,
    #                     'user': user
    #                 }
    #             )
