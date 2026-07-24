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
            service.update_forecast_for_user(user)
        except Exception as e:
            print(f"Failed to update daily forecast for {user}: {e}")


@shared_task
def hourly_weather_and_peaks_check_task():
    now = timezone.localtime(timezone.now())

    if not (6 <= now.hour <= 21):
        print("Celery: Нічний час, оновлення погоди пропущено.")
        return

    service = WeatherForecastService()
    settings_qs = UserProfileSettingsModel.objects.exclude(latitude__isnull=True).exclude(longitude__isnull=True)

    print(f"Celery: Початок щогодинного оновлення погоди для {settings_qs.count()} користувачів...")

    for user_settings in settings_qs:
        user = user_settings.user
        try:
            success = service.update_forecast_for_user(user)
            if success:
                print(f"Celery: Успішно оновлено для {user.username}")
            else:
                print(f"Celery: Не вдалося оновити для {user.username}")
        except Exception as e:
            print(f"Celery Error для {user.username}: {e}")