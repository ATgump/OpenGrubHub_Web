from django.db import models
from django import forms
from django.template.defaultfilters import filesizeformat

# from django.core.exceptions import ValidationError


def mb(n):
    return n * 1048576


class FileField(models.FileField):
    def __init__(self, *args, **kwargs):
        ##self.content_types = kwargs.pop('content_types', [])
        self.max_upload_size = kwargs.pop("max_upload_size", [])
        super(FileField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data = super(FileField, self).clean(*args, **kwargs)
        file = data.file
        try:
            if file.size > self.max_upload_size:
                raise forms.ValidationError(
                    "Please keep filesize under {}. Current filesize {}".format(
                        filesizeformat(self.max_upload_size), filesizeformat(file.size)
                    ),
                    code="invalid",
                )
        except AttributeError:
            pass
        return data
