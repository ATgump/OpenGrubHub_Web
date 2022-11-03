from django.db import models

# Create your models here.
class Comment(models.Model):
    comment = models.TextField(null=True)
    user = models.EmailField(null=True,blank=True)
    #restaurant = models.TextField()