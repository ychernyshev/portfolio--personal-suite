from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from calculator.models import DataEntryLineModel, CurrentTariffModel
from calculator.api.serializers import DataEntrySerializer, CurrentTariffSerializer


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