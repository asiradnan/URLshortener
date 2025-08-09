from django.urls import path
from . import views 
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('api/v1/shorten/',views.shorten, name = 'shorten'),
    path('<str:short_code>/', views.get_actual_url, name = 'get_actual_url'),
    path('api/v1/stats', views.stats, name = 'statistics'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]