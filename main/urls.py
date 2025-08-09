from django.urls import path
from . import views 

urlpatterns = [
    path('shorten/',views.shorten, name = 'shorten'),
    path('<str:short_code>/', views.get_actual_url, name = 'get_actual_url')
]