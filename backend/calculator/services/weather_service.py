# SPDX-License-Identifier: AGPL-3.0-or-later


import datetime
import requests
from django.core.cache import cache
from django.utils import timezone
from calculator.models import CurrentTariffModel, SolarForecastRecordModel, WeatherDataModel, DataEntryLineModel


class WeatherForecastService:
    LAT = 49.8383
    LON = 24.0232
    URL = "https://api.open-meteo.com/v1/forecast"

    def get_solar_forecast(self, current_tariff=None):
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
                "surface_pressure"
            ],
            "timezone": "auto",
            "forecast_days": 1
        }

        try:
            wmo_codes = {
                0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
                45: "Fog", 48: "Depositing rime fog",
                51: "Light drizzle", 53: "Moderate drizzle", 55: "Dense drizzle",
                61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
                71: "Slight snow fall", 73: "Moderate snow fall", 75: "Heavy snow fall",
                80: "Slight rain showers", 81: "Moderate rain showers", 82: "Violent rain showers",
                95: "Thunderstorm",
            }

            response = requests.get(self.URL, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            radiation_data = data.get('hourly', {}).get('shortwave_radiation', [])
            if not radiation_data:
                return {"status": "error", "message": "No radiation data found"}

            today = datetime.date.today()
            year = today.year
            month = today.month
            start_date = datetime.date(year, month, 1)
            yesterday = today - datetime.timedelta(days=1)
            calibration_factor = 1.0

            if yesterday >= start_date:
                actual_qs = DataEntryLineModel.objects.filter(date__range=(start_date, yesterday))
                actual_dict = {q.date.day: float(q.full_day_power) for q in actual_qs if q.full_day_power is not None}

                forecast_qs = SolarForecastRecordModel.objects.filter(date__range=(start_date, yesterday))
                forecast_dict = {q.date.day: float(q.predicted_kwh) for q in forecast_qs if q.predicted_kwh is not None}

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

            current_hour = datetime.datetime.now().hour
            weather_data = data.get('hourly', {})

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
                "current_temp": round(weather_data.get('temperature_2m', [])[current_hour], 1),
                "weather_condition": wmo_codes.get(weather_data.get('weather_code', [])[current_hour], "Unknown"),
                "weather_code": weather_data.get('weather_code', [])[current_hour],
                "calibration_factor": round(calibration_factor, 2)
            }

            cache.set(cache_key, result_dict, 3600)
            self.save_forecast_to_db(result_dict, data)

            return result_dict
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def save_forecast_to_db(self, forecast_data, raw_api_data):
        try:
            today = datetime.date.today()

            SolarForecastRecordModel.objects.update_or_create(
                date=today,
                defaults={
                    'predicted_kwh': forecast_data['predicted_total_kwh'],
                    'predicted_savings': forecast_data['predicted_savings'],
                    'peak_hour': forecast_data['peak_hour'],
                }
            )

            hourly = raw_api_data.get('hourly', {})
            timestamps = hourly.get('time', [])
            temps = hourly.get('temperature_2m', [])
            codes = hourly.get('weather_code', [])
            clouds = hourly.get('cloud_cover', [])
            humidities = hourly.get('relative_humidity_2m', [])
            pressures = hourly.get('surface_pressure', [])

            for i in range(len(timestamps)):
                naive_dt = datetime.datetime.strptime(timestamps[i], '%Y-%m-%dT%H:%M')
                aware_dt = timezone.make_aware(naive_dt)

                WeatherDataModel.objects.update_or_create(
                    timestamp=aware_dt,
                    defaults={
                        'temperature': temps[i],
                        'condition_code': str(codes[i]),
                        'cloud_cover': clouds[i],
                        'humidity': humidities[i],
                        'pressure': pressures[i],
                    }
                )
            return True
        except Exception as e:
            print(f"DB loading error: {e}")
            return False