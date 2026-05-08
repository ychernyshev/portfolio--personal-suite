from django.urls import path, include
from rest_framework.routers import DefaultRouter

from personal.views import ProjectItemViewSet, contact_view

router = DefaultRouter()
router.register('screenshots', ProjectItemViewSet, basename='screenshots')

urlpatterns = [
    path('', include(router.urls)),
    path('contact/', contact_view, name='contact'),
]