from django import forms
from .models import Table

class TableCreateForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ("size","high_seat_compatable")
# class CustomerProfileForm(forms.ModelForm):
#     class Meta:
#         model = CustomerProfile
#         fields = ("date_of_birth",)
