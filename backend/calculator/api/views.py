# SPDX-License-Identifier: AGPL-3.0-or-later


import json
import os
from datetime import datetime, date, timedelta

import requests
from django.http import JsonResponse
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from calculator.api.serializers import (
    DataEntrySerializer,
    CurrentTariffSerializer,
    WeatherConditionSerializer,
    WeatherDataSerializer,
    SolarForecastRecordSerializer,
    GeolocationSerializer, )
from calculator.models import (
    DataEntryLineModel,
    CurrentTariffModel,
    WeatherConditionModel,
    SolarForecastRecordModel,
    WeatherDataModel,
    GeolocationModel, )
from calculator.services.data_export import export_data_logic
from calculator.services.data_import import import_data_logic
from calculator.services.weather_service import WeatherForecastService


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    return Response({'username': request.user.username})


@csrf_exempt
def process_client_weather(request):
    if request.method == 'POST':
        try:
            weather_data = json.loads(request.body)
            service = WeatherForecastService()

            result_dict = service.get_solar_forecast(weather_data)

            return JsonResponse(result_dict)

        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON"}, status=400)
        except Exception as e:
            print(f"Error in process_client_weather: {e}")
            return JsonResponse({"status": "error", "message": str(e)}, status=500)


def current_month():
    return datetime.now().month


class DataEntryViewSet(viewsets.ModelViewSet):
    queryset = DataEntryLineModel.objects.all().order_by('-date')
    serializer_class = DataEntrySerializer

    @action(detail=False, methods=['post'], url_path='import')
    def import_data(self, request):
        result = import_data_logic(request.FILES.get('file'))
        return Response(result, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'], url_path='export')
    def export_data(self, request):
        return export_data_logic(request)


class CurrentTariffViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CurrentTariffModel.objects.all()
    serializer_class = CurrentTariffSerializer

    def get_object(self):
        return CurrentTariffModel.load()


class StatsViewApiView(APIView):
    def get(self, request):
        return Response({
            "total_power": DataEntryLineModel.total_generated_power(),
            "total_cost": DataEntryLineModel.total_cost_power(),
        })


class CurrentMothStatsApiView(APIView):
    def get(self, request):
        entries = DataEntryLineModel.objects.filter(date__month=current_month())

        if not entries.exists():
            return Response({
                "sun_days": 0,
                "average_temperature": 0,
                "average_power": 0,
                "current_month_total_power": 0,
                "current_month_savings": 0,
                "difference_power_percentage": None,
                "is_empty": True
            }, status=200)

        return Response({
            "sun_days": DataEntryLineModel.get_count_of_sun_days(),
            "average_temperature": DataEntryLineModel.get_count_of_month_average_temperature(),
            "average_power": DataEntryLineModel.get_count_of_month_average_power(),
            "current_month_total_power": DataEntryLineModel.get_count_of_month_total_power(),
            "current_month_savings": DataEntryLineModel.get_count_of_month_total_savings(),
            "difference_power_percentage":
                DataEntryLineModel.get_power_difference(),
        })


class DifferenceMonthsStatsApiView(APIView):
    def get(self, request):
        chart_data = DataEntryLineModel.get_monthly_comparison_data()

        if not chart_data:
            return Response({
                "is_empty": True,
                "months_data": []
            }, status=200)

        return Response({
            "is_empty": False,
            "months_data": chart_data
        }, status=200)


class WeatherUpdateTaskView(APIView):
    def get(self, request):
        auth_header = request.headers.get('Authorization')
        cron_secret = os.environ.get('CRON_SECRET')

        if auth_header != f"Bearer {cron_secret}":
            return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            api_url = "https://api.open-meteo.com/v1/forecast"
            coords = GeolocationModel.objects.first()

            if not coords:
                return Response({"error": "No coordinates found in database"}, status=404)

            params = {
                "latitude": coords.latitude,
                "longitude": coords.longitude,
                "hourly": "shortwave_radiation,temperature_2m,weather_code,cloud_cover,relative_humidity_2m,surface_pressure,wind_speed_10m,wind_gusts_10m,wind_direction_10m",
                "daily": "sunrise,sunset",
                "wind_speed_unit": "ms",
                "timezone": "Europe/Kyiv",
                "forecast_days": 1
            }
            response = requests.get(api_url, params=params, timeout=10)
            response.raise_for_status()
            weather_data = response.json()

            service = WeatherForecastService()
            result = service.get_solar_forecast(weather_data)

            return Response({"status": "success", "data": result})
        except Exception as e:
            return Response({"status": "error", "message": str(e)}, status=500)


class WeatherConditionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WeatherConditionModel.objects.all()
    serializer_class = WeatherConditionSerializer


class SolarForecastAPIView(APIView):
    def get(self, request, *args, **kwargs):
        today = timezone.localtime(timezone.now()).date()

        record = SolarForecastRecordModel.objects.filter(date=today).first()

        if record:
            return Response({
                "status": "success",
                "predicted_total_kwh": float(record.predicted_kwh),
                "predicted_savings": float(record.predicted_savings),
                "peak_hour": record.peak_hour,
                "currency": "UAH",
                "wind_speed_10m": float(record.wind_speed_10m) if record.wind_speed_10m else 0.0,
                "wind_gusts_10m": float(record.wind_gusts_10m) if record.wind_gusts_10m else 0.0,
                "wind_direction_10m": record.wind_direction_10m or 0,
            }, status=status.HTTP_200_OK)

        return Response(
            {"status": "error", "message": "No forecast data available for today yet. Please wait for frontend sync."},
            status=status.HTTP_404_NOT_FOUND
        )


class SolarYearAnalyticsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            current_year = date.today().year

            entries = DataEntryLineModel.objects.filter(
                date__year=current_year
            ).prefetch_related('weather')

            categories = {
                "sunny": {"label": "Sunny Days", "days_count": 0, "total_power": 0.0, "total_cost": 0.0},
                "cloudy": {"label": "Cloudy Days", "days_count": 0, "total_power": 0.0, "total_cost": 0.0},
                "rain_snow": {"label": "Rain / Snow", "days_count": 0, "total_power": 0.0, "total_cost": 0.0},
                "other": {"label": "Other Weather", "days_count": 0, "total_power": 0.0, "total_cost": 0.0},
            }

            for entry in entries:
                weather_names = [w.name.lower() for w in entry.weather.all()]

                try:
                    power = float(entry.full_day_power) if entry.full_day_power is not None else 0.0
                except (TypeError, ValueError):
                    power = 0.0

                try:
                    cost = float(entry.full_day_cost) if entry.full_day_cost is not None else 0.0
                except (TypeError, ValueError):
                    cost = 0.0

                if any("sunny" in name for name in weather_names):
                    categories["sunny"]["days_count"] += 1
                    categories["sunny"]["total_power"] += power
                    categories["sunny"]["total_cost"] += cost

                elif any("cloudy" in name for name in weather_names):
                    categories["cloudy"]["days_count"] += 1
                    categories["cloudy"]["total_power"] += power
                    categories["cloudy"]["total_cost"] += cost

                elif any("rain" in name or "snow" in name for name in weather_names):
                    categories["rain_snow"]["days_count"] += 1
                    categories["rain_snow"]["total_power"] += power
                    categories["rain_snow"]["total_cost"] += cost

                else:
                    categories["other"]["days_count"] += 1
                    categories["other"]["total_power"] += power
                    categories["other"]["total_cost"] += cost

            for key in categories:
                categories[key]["total_power"] = round(categories[key]["total_power"], 2)
                categories[key]["total_cost"] = round(categories[key]["total_cost"], 2)

            response_data = {
                "year": current_year,
                "categories": categories
            }

            return Response(response_data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": "Failed to calculate analytics", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class SolarMonthAnalyticsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            today = date.today()
            year = today.year
            month = today.month

            start_date = date(year, month, 1)
            if month == 12:
                end_date = date(year + 1, 1, 1) - timedelta(days=1)
            else:
                end_date = date(year, month + 1, 1) - timedelta(days=1)

            total_days = end_date.day

            actual_qs = DataEntryLineModel.objects.filter(date__range=(start_date, today))
            actual_dict = {
                q.date.day: round(float(q.full_day_power) / 1000.0, 2)
                for q in actual_qs if q.full_day_power is not None
            }

            forecast_qs = SolarForecastRecordModel.objects.filter(date__range=(start_date, today))
            forecast_dict = {q.date.day: float(q.predicted_kwh) for q in forecast_qs if q.predicted_kwh is not None}

            api_forecast_dict = {}
            if today < end_date:
                system_factor = 3.45 * 0.23 * 0.85

                api_url = "https://api.open-meteo.com/v1/forecast"
                params = {
                    "latitude": 49.8383,
                    "longitude": 24.0232,
                    "hourly": "shortwave_radiation",
                    "timezone": "auto",
                    "forecast_days": 16
                }

                response = requests.get(api_url, params=params, timeout=10)
                if response.status_code == 200:
                    api_data = response.json()
                    rad_data = api_data.get('hourly', {}).get('shortwave_radiation', [])
                    times = api_data.get('hourly', {}).get('time', [])

                    total_real = 0.0
                    total_pred_db = 0.0

                    for day_idx in actual_dict.keys():
                        if day_idx in forecast_dict and forecast_dict[day_idx] > 0:
                            total_real += actual_dict[day_idx]
                            total_pred_db += forecast_dict[day_idx]

                    calibration_factor = 1.0
                    if total_pred_db > 0 and total_real > 0:
                        calibration_factor = total_real / total_pred_db

                    base_system_factor = 3.45 * 0.23 * 0.85

                    calibrated_factor = base_system_factor * calibration_factor

                    for i in range(min(len(times), len(rad_data))):
                        if rad_data[i] is None:
                            continue

                        dt = datetime.strptime(times[i][:10], "%Y-%m-%d").date()

                        if dt.month == month and dt.year == year:
                            day_num = dt.day
                            wh = float(rad_data[i]) * calibrated_factor

                            if day_num not in api_forecast_dict:
                                api_forecast_dict[day_num] = 0.0
                            api_forecast_dict[day_num] += wh

                    for day_num in list(api_forecast_dict.keys()):
                        if api_forecast_dict[day_num] <= 0:
                            del api_forecast_dict[day_num]
                        else:
                            api_forecast_dict[day_num] = round(api_forecast_dict[day_num] / 1000, 2)

            labels = []
            actual_power = []
            forecast_power = []

            for day in range(1, total_days + 1):
                labels.append(day)

                if day <= today.day:
                    actual_power.append(actual_dict.get(day, None))
                else:
                    actual_power.append(None)

                if day in api_forecast_dict:
                    forecast_power.append(api_forecast_dict[day])
                elif day in forecast_dict:
                    forecast_power.append(round(forecast_dict[day], 2))
                else:
                    forecast_power.append(None)

            result = {
                "status": "success",
                "month_name": today.strftime("%B"),
                "labels": labels,
                "actual_power": actual_power,
                "forecast_power": forecast_power
            }

            return Response(result, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"status": "error", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SolarComparisonAPIView(APIView):
    def get(self, request):
        records = SolarForecastRecordModel.objects.all()[:7]
        data = []

        for r in records:
            actual = r.get_actual_data()
            data.append({
                "date": r.date,
                "predicted": r.predicted_kwh,
                "actual": round(actual.full_day_power / 1000, 2) if actual else 0,
                "accuracy": r.accuracy_percentage,
                "savings_diff": round(actual.full_day_cost - r.predicted_savings, 2) if actual else 0
            })

        return Response(data)


class WeatherDataViewSet(viewsets.ModelViewSet):
    queryset = WeatherDataModel.objects.all()
    serializer_class = WeatherDataSerializer


class SolarForecastRecordViewSet(viewsets.ModelViewSet):
    serializer_class = SolarForecastRecordSerializer

    def get_queryset(self):
        queryset = SolarForecastRecordModel.objects.all()
        date_param = self.request.query_params.get('date')

        if date_param:
            naive_dt = parse_datetime(date_param)
            if naive_dt:
                aware_dt = timezone.make_aware(naive_dt)
                queryset = queryset.filter(date=aware_dt.date())

        return queryset.order_by('-date')


class GeolocationViewSet(viewsets.ModelViewSet):
    queryset = GeolocationModel.objects.all()
    serializer_class = GeolocationSerializer
