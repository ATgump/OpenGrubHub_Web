from django.db import models
from .fields import mb,FileField
from .validators import validate_file_extension
# Create your models here.

# class Png(models.Model):
#     file = models.FileField(
#         upload_to="png",
#         content_types=['image/png'],
#         max_upload_size=mb(5),
#     )

##Switch to All Files with no Type Checking

class Css(models.Model):
    file = FileField(
        upload_to='css/', 
        #content_types=['text/css','text/plain'],
        validators = [validate_file_extension],
        max_upload_size=mb(5),
        blank=True,
        null=True,
    )