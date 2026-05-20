from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# ДОДАЄМО ЦЕЙ ІМПОРТ НАПРЯМУ:
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/auth/jwt/create', TokenObtainPairView.as_view(), name='token_obtain_pair_noslash'),
    path('api/auth/jwt/create/', TokenObtainPairView.as_view(), name='token_obtain_pair_slash'),
    path('api/auth/jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),

    path('api/personal/', include(('personal.urls', 'personal'), namespace='personal')),
    path('calculator/', include('calculator.api.urls')),  # App V1
    path('api/calculator/', include(('calculator.api.urls', 'calculator'), namespace='calculator')),  # App V2
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)