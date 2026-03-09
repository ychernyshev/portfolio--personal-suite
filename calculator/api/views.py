from rest_framework import viewsets
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