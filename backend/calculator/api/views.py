import io
import os

import pandas as pd
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