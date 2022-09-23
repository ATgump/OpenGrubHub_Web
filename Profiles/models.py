from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

## Change this to extend the User model
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    AUTH_PROFILE_MODULE='app.Profile'
    MEMBER = 1
    AUTH_MEMBER =2
    EXEC = 3
    birth_date = models.DateField(null=True,blank=True)
    ROLE_CHOICES = (
        (MEMBER,"Member"),
        (EXEC, "Executive"),
        (AUTH_MEMBER,"Authorized Member"),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES,unique=False,default=1)
    def __str__(self):
        return self.user.username
    def get_absolute_url(self):
        #print(str(self))
        return reverse("Profiles:memberProfile", kwargs={"user":str(self)}) #f"/user_profiles/{self.id}" ### do this to make sure links update

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

@receiver(post_save,sender=User)
def update_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()