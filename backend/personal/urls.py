from django.urls import path, include
from rest_framework.routers import DefaultRouter

from personal.views import (
    ProjectItemViewSet,
    ContactMessageViewSet
)

router = DefaultRouter()
router.register('projects', ProjectItemViewSet, basename='projects')
router.register('user/admin/emails/inbound', ContactMessageViewSet, basename='email')
router.register('contact', ContactMessageViewSet, basename='contact')

urlpatterns = [
    path('', include(router.urls)),
]
