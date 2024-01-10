# weather_api_app/models.py
from django.db import models

class WeatherCache(models.Model):
    city = models.CharField(max_length=255, unique=True)
    temperature = models.FloatField()
    pressure = models.FloatField()
    wind_speed = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city} - {self.timestamp}"
