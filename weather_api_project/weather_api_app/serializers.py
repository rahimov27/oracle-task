# weather_api_app/serializers.py
from rest_framework import serializers
from .models import WeatherCache

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherCache
        fields = ['city', 'temperature', 'pressure', 'wind_speed', 'timestamp']
