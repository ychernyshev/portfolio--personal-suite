from django.urls import path, include
from rest_framework.routers import DefaultRouter
from calculator.api.views import (DataEntryViewSet,
                                  CurrentTariffViewSet,
                                  StatsViewApiView,
                                  WeatherConditionViewSet,
                                  SolarForecastAPIView,
                                  SolarComparisonAPIView)

router = DefaultRouter()
router.register(r'entries', DataEntryViewSet, basename='entries')
router.register(r'weather-conditions', WeatherConditionViewSet, basename='weather-conditions')

urlpatterns = [
    path('', include(router.urls)),
    path('current-tariff/', CurrentTariffViewSet.as_view({'get': 'retrieve'}), name='current-tariff'),
    path('stats/', StatsViewApiView.as_view(), name='stats'),
    path('forecast/', SolarForecastAPIView.as_view(), name='forecast'),
    path('forecast/comparison/', SolarComparisonAPIView.as_view(), name='comparison'),
    path('data-export/', SolarForecastAPIView.as_view(), name='data-export'),
    path('data-import/', SolarForecastAPIView.as_view(), name='data-import'),
]