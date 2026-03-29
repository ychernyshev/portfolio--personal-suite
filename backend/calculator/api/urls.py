from django.urls import path, include
from rest_framework.routers import DefaultRouter
from calculator.api.views import (DataEntryViewSet,
                                  CurrentTariffViewSet,
                                  StatsViewApiView,
                                  WeatherConditionViewSet,
                                  SolarForecastAPIView,
                                  SolarComparisonAPIView)
from calculator.services.data_import import data_import
from calculator.services.data_export import data_export

router = DefaultRouter()
router.register(r'entries', DataEntryViewSet, basename='entries')
router.register(r'weather-conditions', WeatherConditionViewSet, basename='weather-conditions')

urlpatterns = [
    path('', include(router.urls)),
    path('current-tariff/', CurrentTariffViewSet.as_view({'get': 'retrieve'}), name='current-tariff'),
    path('stats/', StatsViewApiView.as_view(), name='stats'),
    path('solar-forecast/', SolarForecastAPIView.as_view(), name='solar-forecast'),
    path('solar-comparison/', SolarComparisonAPIView.as_view(), name='solar-comparison'),
    path('data-export/', data_export, name='data-export'),
    path('data-import/', data_import, name='data-import'),
]