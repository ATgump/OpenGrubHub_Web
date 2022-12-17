from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from Profiles.models import User
# Model for reservation system
class ReservationModel(models.Model):
    first_name = models.CharField(null=True, max_length=120)
    last_name = models.CharField(null=True, max_length = 120)
    email = models.EmailField(null=True)
    phone_number = PhoneNumberField(null=False, blank=False)
    time = models.TimeField(null=True)
    date = models.DateField(null=True)
    table_size = models.PositiveSmallIntegerField(null=True)
    high_seat = models.BooleanField(null=True)

    ## Each Reservation must have 1 restaurant and customer, (many to one)
    restaurant = models.ForeignKey(User,on_delete=models.CASCADE,related_name="restaurant",null=True)
    customer = models.ForeignKey(User,on_delete=models.CASCADE,related_name="customer",null=True)

    ## get absolute url to allow displaying of individual reservation details
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("ReservationApp:reservation-detail", kwargs={"pk": self.id})