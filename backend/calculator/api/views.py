import io
import os
from datetime import datetime, date, timedelta

import pandas as pd
import requests
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from calculator.api.serializers import DataEntrySerializer, CurrentTariffSerializer, WeatherConditionSerializer, \
    WeatherDataSerializer
from calculator.models import DataEntryLineModel, CurrentTariffModel, WeatherConditionModel, SolarForecastRecordModel, WeatherDataModel
from calculator.services.data_export import export_data_logic
from calculator.services.data_import import import_data_logic
from calculator.services.weather_service import WeatherForecastService


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
    """Тариф можна тільки читати через API (або додати Update)"""
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

        service = WeatherForecastService()
        result = service.get_solar_forecast()

        return Response({"status": "success", "data": result})


class WeatherConditionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WeatherConditionModel.objects.all()
    serializer_class = WeatherConditionSerializer


class SolarForecastAPIView(APIView):
    def get(self, request, *args, **kwargs):
        service = WeatherForecastService()
        forecast_data = service.get_solar_forecast()

        if forecast_data.get("status") == "success":
            return Response(forecast_data, status=status.HTTP_200_OK)

        return Response(
            {"error": forecast_data.get("message", "Unknown error")},
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