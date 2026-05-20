from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),

    path(
        'api/auth/jwt/create/',
        TokenObtainPairView.as_view(
            permission_classes=[AllowAny],
            authentication_classes=[]
        ),
        name='token_create_override'
    ),
    path(
        'api/auth/jwt/create',
        TokenObtainPairView.as_view(
            permission_classes=[AllowAny],
            authentication_classes=[]
        ),
        name='token_create_override_no_slash'
    ),

    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
    path('api/personal/', include(('personal.urls', 'personal'), namespace='personal')),
    path('calculator/', include('calculator.api.urls')),  # App V1
    path('api/calculator/', include(('calculator.api.urls', 'calculator'), namespace='calculator')),  # App V2
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
