from django.urls import path, include
from rest_framework.routers import DefaultRouter

from personal.views import ProjectItemViewSet, contact_view, ContactMessageViewSet

router = DefaultRouter()
router.register('projects', ProjectItemViewSet, basename='projects')
router.register('inbound-messages', ContactMessageViewSet, basename='inbound-messages')

urlpatterns = [
    path('', include(router.urls)),
    path('contact/', contact_view, name='contact'),
]