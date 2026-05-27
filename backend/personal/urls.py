from django.urls import path, include
from rest_framework.routers import DefaultRouter

from personal.views import (
    ProjectItemViewSet,
    ContactMessageViewSet,
    SetMessageStatusViewSet
)

router = DefaultRouter()
router.register('projects', ProjectItemViewSet, basename='projects')
router.register('user/dashboard/mail/inbound', ContactMessageViewSet, basename='email')
router.register('user/mail/status', SetMessageStatusViewSet, basename='mail_status')
router.register('contact', ContactMessageViewSet, basename='contact')

urlpatterns = [
    path('', include(router.urls)),
]
