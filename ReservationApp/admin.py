from django.contrib import admin
from .models import ReservationModel
# Register your models here.

admin.site.register(ReservationModel)

## Allow admin to delete reservations
class ProfileInline(admin.StackedInline):
    model = ReservationModel
    can_delete = False
    verbose_name_plural = "Reservation"

