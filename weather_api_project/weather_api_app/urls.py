# weather_api_app/urls.py
from django.urls import path
from .views import WeatherAPIView

urlpatterns = [
    path('weather/', WeatherAPIView.as_view(), name='weather'),
]
