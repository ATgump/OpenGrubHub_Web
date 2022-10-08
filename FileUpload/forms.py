from .models import Css
from django import forms


class CssCreateForm(forms.ModelForm):
    class Meta:
        model = Css
        fields = ["file"]
