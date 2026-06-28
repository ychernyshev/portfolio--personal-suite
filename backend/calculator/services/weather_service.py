# SPDX-License-Identifier: AGPL-3.0-or-later

import asyncio
import datetime
import httpx
import os
from calculator.models import CurrentTariffModel, SolarForecastRecordModel, WeatherDataModel, DataEntryLineModel
from django.core.cache import cache
from django.utils import timezone


class WeatherForecastService:
    LAT = 49.8383
    LON = 24.0232
    URL = "https://api.open-meteo.com/v1/forecast"
    VERCEL_PROXY_URL = os.getenv("VERCEL_PROXY_URL")

    async def _fetch_api(self, client, url, params, source_name):
        if not url:
            print(f"WeatherService: URL for {source_name} is empty or not set.")
            return None
        try:
            response = await client.get(url, params=params, timeout=4.0)
            if response.status_code == 200:
                print(f"WeatherService: {source_name} WON the race!")
                return response.json()
            else:
                print(f"WeatherService: {source_name} returned status {response.status_code}")
                return None
        except Exception as e:
            print(f"WeatherService: {source_name} failed during race: {e}")
            return None

    async def _race_requests(self, params):
        async with httpx.AsyncClient() as client:
            task_primary = asyncio.create_task(self._fetch_api(client, self.URL, params, "Primary Open-Meteo"))
            task_backup = asyncio.create_task(self._fetch_api(client, self.VERCEL_PROXY_URL, params, "Vercel Proxy"))

            pending = {task_primary, task_backup}

            while pending:
                done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)

                for completed_task in done:
                    result = completed_task.result()
                    if result is not None:
                        for active_task in pending:
                            active_task.cancel()
                        return result
            return None

    def get_solar_forecast(self, current_tariff=None, user_timezone="Europe/Kyiv"):
        cache_key = 'solar_forecast_lviv'
        cached_data = cache.get(cache_key)

        if cached_data:
            return cached_data

        if current_tariff is None:
            current_tariff = CurrentTariffModel.load().power_tariff

        params = {
            "latitude": self.LAT,
            "longitude": self.LON,
            "hourly": [
                "shortwave_radiation",
                "temperature_2m",
                "weather_code",
                "cloud_cover",
                "relative_humidity_2m",
                "surface_pressure",
                "wind_speed_10m",
                "wind_gusts_10m",
                "wind_direction_10m",
            ],
            "daily": [
                "sunrise",
                "sunset",
            ],
            "wind_speed_unit": "ms",
            "timezone": user_timezone,
            "forecast_days": 1
        }

        wmo_codes = {
            0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
            45: "Fog", 48: "Depositing rime fog",
            51: "Light drizzle", 53: "Moderate drizzle", 55: "Dense drizzle",
            61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
            71: "Slight snow fall", 73: "Moderate snow fall", 75: "Heavy snow fall",
            80: "Slight rain showers", 81: "Moderate rain showers", 82: "Violent rain showers",
            95: "Thunderstorm",
        }

        try:
            data = asyncio.run(self._race_requests(params))
        except Exception as race_error:
            print(f"WeatherService: Race crashed entirely: {race_error}")
            data = None

        if data and data.get('hourly', {}).get('shortwave_radiation'):
            try:
                radiation_data = data['hourly']['shortwave_radiation']
                today = datetime.date.today()
                year = today.year
                month = today.month
                start_date = datetime.date(year, month, 1)
                yesterday = today - datetime.timedelta(days=1)
                calibration_factor = 1.0

                if yesterday >= start_date:
                    actual_qs = DataEntryLineModel.objects.filter(date__range=(start_date, yesterday))
                    actual_dict = {q.date.day: float(q.full_day_power) for q in actual_qs if
                                   q.full_day_power is not None}

                    forecast_qs = SolarForecastRecordModel.objects.filter(date__range=(start_date, yesterday))
                    forecast_dict = {q.date.day: float(q.predicted_kwh) for q in forecast_qs if
                                     q.predicted_kwh is not None}

                    total_real = 0.0
                    total_pred = 0.0

                    for day_idx in actual_dict.keys():
                        if day_idx in forecast_dict and forecast_dict[day_idx] > 0:
                            real_kwh = actual_dict[day_idx] / 1000.0
                            total_real += real_kwh
                            total_pred += forecast_dict[day_idx]

                    if total_pred > 0 and total_real > 0:
                        calibration_factor = total_real / total_pred

                total_area = 3.45
                panel_efficiency = 0.23
                performance_ratio = 0.85

                system_factor = total_area * panel_efficiency * performance_ratio * calibration_factor
                hourly_gen_wh = [round(rad * system_factor, 2) for rad in radiation_data]

                weather_data = data.get('hourly', {})
                wind_speeds = weather_data.get('wind_speed_10m', [])
                wind_gusts = weather_data.get('wind_gusts_10m', [])
                wind_directions = weather_data.get('wind_direction_10m', [])

                avg_speed = round(sum(wind_speeds) / len(wind_speeds), 1) if wind_speeds else 0.0
                max_gust = max(wind_gusts) if wind_gusts else 0.0
                avg_direction = int(sum(wind_directions) / len(wind_directions)) if wind_directions else 0

                current_hour = datetime.datetime.now().hour
                weather_data = data.get('hourly', {})

                temp_list = weather_data.get('temperature_2m', [])
                code_list = weather_data.get('weather_code', [])

                safe_hour = min(current_hour, len(temp_list) - 1) if temp_list else 0

                current_temp = round(temp_list[safe_hour], 1) if temp_list else 0.0
                weather_condition = wmo_codes.get(code_list[safe_hour], "Unknown") if code_list else "Unknown"
                weather_code = code_list[safe_hour] if code_list else 0

                total_kwh = sum(hourly_gen_wh) / 1000
                predicted_savings = total_kwh * current_tariff

                result_dict = {
                    "predicted_total_kwh": round(total_kwh, 2),
                    "predicted_savings": round(predicted_savings, 2),
                    "hourly_forecast_wh": hourly_gen_wh,
                    "currency": "UAH",
                    "peak_hour": radiation_data.index(max(radiation_data)) if radiation_data else 0,
                    "status": "success",
                    "tariff_used": current_tariff,
                    "current_temp": current_temp,
                    "weather_condition": weather_condition,
                    "weather_code": weather_code,
                    "calibration_factor": round(calibration_factor, 2),
                    "wind_speed_10m": avg_speed,
                    "wind_gusts_10m": max_gust,
                    "wind_direction_10m": avg_direction
                }

                cache.set(cache_key, result_dict, 3600)
                self.save_forecast_to_db(result_dict, data)

                return result_dict
            except Exception as calc_error:
                print(f"WeatherService: Error during calculation: {calc_error}")

        print("WeatherService: Both APIs failed the race or returned invalid data. Activating DB Fallback.")
        today = datetime.date.today()
        last_record = SolarForecastRecordModel.objects.filter(date=today).first()
        if not last_record:
            last_record = SolarForecastRecordModel.objects.order_by('-date').first()

        if last_record:
            return {
                "predicted_total_kwh": float(last_record.predicted_kwh),
                "predicted_savings": float(last_record.predicted_savings),
                "hourly_forecast_wh": [0.0] * 24,
                "currency": "UAH",
                "peak_hour": int(last_record.peak_hour),
                "status": "fallback",
                "tariff_used": current_tariff,
                "current_temp": 0.0,
                "weather_condition": "APIs High Latency (DB Cache)",
                "weather_code": 0,
                "calibration_factor": 1.0
            }

        return {
            "predicted_total_kwh": 0.0, "predicted_savings": 0.0, "hourly_forecast_wh": [0.0] * 24,
            "currency": "UAH", "peak_hour": 0, "status": "error", "tariff_used": current_tariff,
            "current_temp": 0.0, "weather_condition": "Unavailable", "weather_code": 0, "calibration_factor": 1.0
        }

    def convert_iso_to_datetime(self, data):
        sunrise_str = data['daily']['sunrise'][0]
        sunset_str = data['daily']['sunset'][0]

        sunrise_dt = datetime.datetime.fromisoformat(sunrise_str)
        sunset_dt = datetime.datetime.fromisoformat(sunset_str)

        return sunrise_dt, sunset_dt

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
                    'predicted_kwh': forecast_data['predicted_total_kwh'],
                    'predicted_savings': forecast_data['predicted_savings'],
                    'peak_hour': forecast_data['peak_hour'],
                    'sunrise': sunrise_dt,
                    'sunset': sunset_dt,
                    'wind_speed_10m': avg_speed,
                    'wind_gusts_10m': max_gust,
                    'wind_direction_10m': avg_direction
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
            pressures = hourly.get('surface_pressure', [])

            parsed_timestamps = []
            for ts in timestamps:
                naive_dt = datetime.datetime.strptime(ts, '%Y-%m-%dT%H:%M')
                parsed_timestamps.append(timezone.make_aware(naive_dt))

            WeatherDataModel.objects.filter(timestamp__in=parsed_timestamps).delete()

            weather_objects = []
            for i in range(len(timestamps)):
                weather_objects.append(
                    WeatherDataModel(
                        timestamp=parsed_timestamps[i],
                        temperature=temps[i],
                        condition_code=str(codes[i]),
                        cloud_cover=clouds[i],
                        humidity=humidities[i],
                        pressure=pressures[i],
                    )
                )

            WeatherDataModel.objects.bulk_create(weather_objects)
            return True

        except Exception as e:
            print(f"DB loading error: {e}")
            return False
