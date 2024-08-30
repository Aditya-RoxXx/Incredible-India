import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class City(models.Model):
    city_name = models.CharField(max_length=50)
    city_state = models.CharField(max_length=50)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.city_name
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class CityDescription(models.Model):
    name = models.ForeignKey(City, on_delete=models.CASCADE)
    city_description = models.CharField(max_length=1000)
    best_food = models.CharField(max_length=100)
    best_place_to_visit = models.CharField(max_length=200)
    rating = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.city_description
