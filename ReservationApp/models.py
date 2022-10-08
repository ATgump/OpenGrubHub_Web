from django.db import models

# Create your models here.


class ReservationModel(models.Model):
    time = models.TimeField(null=True)
    date = models.DateField(null=True)
    number_of_customers = models.PositiveSmallIntegerField()
