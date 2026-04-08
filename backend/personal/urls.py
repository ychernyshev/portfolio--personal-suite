from django.urls import path, include
from rest_framework.routers import DefaultRouter

from personal.views import ProjectItemViewSet

router = DefaultRouter()
router.register('projects', ProjectItemViewSet, basename='projects')

urlpatterns = [
    path('', include(router.urls)),
]