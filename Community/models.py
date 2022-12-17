from django.db import models

# Create your models here.


#Model for our comments
class Comment(models.Model):
    comment = models.TextField(null=True)
    user = models.CharField(max_length = 500,null=True,blank=True)
    create_time = models.DateTimeField(null=True,auto_now_add=True)