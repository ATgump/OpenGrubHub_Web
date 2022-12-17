from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_google_maps import fields as map_fields
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating
from django.utils.translation import gettext as _
## Change this to extend the User model
## New user manager so I could get email to be the main field not username (we dont want usernames just emails)
class UserManager(UserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True
 
    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_customer',True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    ## Field for checking if a user is a customer or restaurant
    is_customer = models.BooleanField(default=False)
    email = models.EmailField(_('email address'), unique=True, blank=True,error_messages={
            'unique': _("A user with that email already exists."),
        })
    username = models.CharField(_('username'), max_length=30,
        error_messages={
            'unique': _("A user with that username already exists."),
        })
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    def __str__(self):
        if self.is_customer:
            return self.email
        else:
            return self.restaurant_profile.restaurant_name 

class CustomerProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="customer_profile", null=True
    )
    date_of_birth = models.DateField(null=True, blank=True)
    ## Define how to get absolute url to get customer profile
    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("Profiles:CustomerProfile", kwargs={"id": self.user.id})

class RestaurantProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="restaurant_profile", null=True
    )
    ## Restuarant address, lat, long, ratings, and name
    restaurant_address = map_fields.AddressField(max_length=200, null=True)
    lat = models.DecimalField(max_digits=22,decimal_places=16,null=True)
    long = models.DecimalField(max_digits=22,decimal_places=16,null=True)
    ratings = GenericRelation(Rating, related_query_name='ratings')


    restaurant_name = models.CharField(_('restuarant name'), max_length=60, null=True)
    ## Define how to get absolute url to get Restaurant profile
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("Profiles:RestaurantProfile", kwargs={"id": self.user.id})
    ## Define how to get absolute url to get Restaurant profile management section
    def get_absolute_url_manage(self):
        from django.urls import reverse
        return reverse("Profiles:RestaurantManage", kwargs={"id": self.user.id})


### Signal for handling saving the profiles when the user is created
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
