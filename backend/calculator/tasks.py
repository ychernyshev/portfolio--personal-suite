# SPDX-License-Identifier: AGPL-3.0-or-later
from celery import shared_task
from django.contrib.auth import get_user_model
from django.utils import timezone

from calculator.models import UserProfileSettingsModel
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


@shared_task
def hourly_weather_and_peaks_check_task():
    service = WeatherForecastService()

    settings_qs = UserProfileSettingsModel.objects.exclude(latitude__isnull=True).exclude(longitude__isnull=True)

    for user_settings in settings_qs:
        user = user_settings.user
        print(f"Celery: Оновлення прогнозу для користувача {user.username}...")
        service.update_forecast_for_user(user)


@shared_task
def hourly_weather_check_task():
    now = timezone.localtime(timezone.now())
    if 6 <= now.hour <= 21:
        service = WeatherForecastService()