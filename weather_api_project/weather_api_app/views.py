# weather_api_app/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import WeatherCache
from .serializers import WeatherSerializer
import requests
from datetime import datetime, timedelta

class WeatherAPIView(APIView):
    def get(self, request):
        city = request.GET.get('city', '')
        if not city:
            return Response({'error': 'City parameter is missing'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if data is cached
        cached_data = WeatherCache.objects.filter(city=city, timestamp__gte=datetime.now() - timedelta(minutes=30)).first()

        if cached_data:
            serializer = WeatherSerializer(cached_data)
            return Response(serializer.data)

        # Fetch data from openweathermap.com
        openweathermap_api_key = '0b52a5b549b387b411cb1955969d0978'  # Replace with your actual API key
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': city,
            'appid': openweathermap_api_key,
            'units': 'metric',
        }
        response = requests.get(base_url, params=params)
        data = response.json()

        if 'main' in data and 'wind' in data:
            # Cache the data
            weather_data = {
                'city': city,
                'temperature': data['main']['temp'],
                'pressure': data['main']['pressure'],
                'wind_speed': data['wind']['speed'],
            }
            serializer = WeatherSerializer(data=weather_data)
            if serializer.is_valid():
                serializer.save()

            return Response(serializer.data)
        else:
            return Response({'error': 'Failed to fetch weather data'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
