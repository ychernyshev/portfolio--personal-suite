# SPDX-License-Identifier: AGPL-3.0-or-later
from celery import shared_task
from django.contrib.auth import get_user_model

from calculator.services.weather_service import WeatherForecastService


@shared_task
def run_daily_forecast_update():
    User = get_user_model()
    service = WeatherForecastService()

    for user in User.objects.filter(geolocation__isnull=False):
        try:
            service.get_solar_forecast(data=None, user=user)
        except Exception as e:
            print(f"Failed to update forecast for {user}: {e}")