from django.db import models

# Create your models here.
class PermissionList(models.Model):
    name = models.CharField(max_length=64)
    url = models.CharField(max_length=255)
    def __unicode__(self):
        return '%s(%s)' % (self.name, self.url)


class RoleList(models.Model):
    name = models.CharField(max_length=64)
    permission = models.ManyToManyField(PermissionList, null=True, blank=True)
    def __unicode__(self):
        return self.name
