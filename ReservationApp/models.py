from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class ReservationModel(models.Model):
    first_name = models.CharField(null=True, max_length=120)
    last_name = models.CharField(null=True, max_length = 120)
    email = models.EmailField(null=True)
    phone_number = PhoneNumberField(null=False, blank=False)
    time = models.TimeField(null=True)
    date = models.DateField(null=True)
    table_size = models.PositiveSmallIntegerField(null=True)
    high_seat = models.BooleanField(null=True)
