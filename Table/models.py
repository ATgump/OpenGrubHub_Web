from django.db import models
from Profiles.models import RestaurantProfile
# Create your models here
class Table(models.Model):
    size = models.PositiveSmallIntegerField()
    high_seat_compatable = models.BooleanField()
    restaurant = models.ForeignKey(RestaurantProfile,on_delete=models.CASCADE)
    ##unavailable = models.JSONField() ## work on this, for setting the tables availability
