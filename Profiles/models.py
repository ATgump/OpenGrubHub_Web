from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_google_maps import fields as map_fields

## Change this to extend the User model


class User(AbstractUser):
    is_customer = models.BooleanField(default=False)

    def __str__(self):
        if self.is_customer:
            return self.username
        else:
            return self.username  ## change this to restaurant name when this is setup

    # def get_absolute_url(self):
    #     print("called this")
    #     if self.is_customer:
    #         return reverse("Profiles:CustomerProfile", kwargs={"id":self.id}) #f"/user_profiles/{self.id}" ### do this to make sure links update
    #     else:
    #         print("called this2")
    #         return reverse("Profiles:RestaurantProfile", kwargs={"id":self.id})

    ## add more roles if needed
    # USER_TYPE_CHOICES = (
    #     (1,"customer"),
    #     (2,"restaurant"),
    # )
    # user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    # roles = models.ManyToManyField(Role)


class CustomerProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="customer_profile", null=True
    )
    # AUTH_PROFILE_MODULE='app.CustomerProfile'
    # Customer Fields
    birth_date = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("Profiles:CustomerProfile", kwargs={"id": self.user.id})

    # def __str__(self):
    #     return self.user.username
    # def get_absolute_url(self):
    #     return reverse("Profiles:memberProfile", kwargs={"user":str(self)}) #f"/user_profiles/{self.id}" ### do this to make sure links update


class RestaurantProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="restaurant_profile", null=True
    )

    # AUTH_PROFILE_MODULE='app.RestaurantProfile'
    ## Restaurant Specific Fields
    address = map_fields.AddressField(max_length=200, null=True)
    geolocation = map_fields.GeoLocationField(max_length=100, null=True)
    # address = AddressField(null=True)
    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("Profiles:RestaurantProfile", kwargs={"id": self.user.id})

    # def __str__(self):
    #     return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if instance.is_customer:
        if created:
            CustomerProfile.objects.get_or_create(user=instance)
        instance.customer_profile.save()
    else:
        if created:
            RestaurantProfile.objects.get_or_create(user=instance)
        instance.restaurant_profile.save()
