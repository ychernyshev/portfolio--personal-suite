from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from calculator.models import DataEntryLineModel, CurrentTariffModel, WeatherConditionModel, SolarForecastRecord
from calculator.api.serializers import DataEntrySerializer, CurrentTariffSerializer, WeatherConditionSerializer

from calculator.services.weather_service import WeatherForecastService


class DataEntryViewSet(viewsets.ModelViewSet):
    queryset = DataEntryLineModel.objects.all().order_by('-date')
    serializer_class = DataEntrySerializer


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
        records = SolarForecastRecord.objects.all()[:7]
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