from django.urls import path, include
from rest_framework.routers import DefaultRouter
from calculator.api.views import DataEntryViewSet, CurrentTariffViewSet

router = DefaultRouter()
router.register(r'entries', DataEntryViewSet, basename='entries')

urlpatterns = router.urls

# urlpatterns = [
#     path('', include(router.urls)),
#     path('current-tariff/', CurrentTariffViewSet.as_view({'get': 'retrieve'})),
# ]