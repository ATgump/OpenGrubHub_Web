from django import forms
from django.db import models, transaction
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from Profiles.models import CustomerProfile, RestaurantProfile, User
from django.contrib.auth import authenticate
from django_google_maps import widgets as map_widgets
import json
import uuid
import requests
from django.conf import settings


class UserLoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user) -> None:
        if not user.is_active:
            raise forms.ValidationError(
                ("This account is inactive."),
                code="inactive",
            )
        return super().confirm_login_allowed(user)


### Update these forms for the user create Page
class UserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(
            render_value=True, attrs={"class": "autocomplete-items2"}
        ),
        required=True,
    )
    password_confirmation = forms.CharField(
        widget=forms.PasswordInput(
            render_value=True, attrs={"class": "autocomplete-items2"}
        ),
        required=True,
    )

    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "password",
            "password_confirmation",
        )

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")
        email = cleaned_data.get("email")
        if password != password_confirmation:
            self.fields["password"].widget = forms.PasswordInput(
                attrs={"class": "autocomplete-items2"}
            )
            self.fields["password_confirmation"].widget = forms.PasswordInput(
                attrs={"class": "autocomplete-items2"}
            )

            self.add_error("password", "Must match with Password confirmation")
            self.add_error("password_confirmation", "Must match with Password")
            raise forms.ValidationError(
                "Password and Password confirmation do not match"
            )
        elif User.objects.filter(email=email).exists():
            self.fields["email"].widget = forms.TextInput()
            self.add_error("email", "User Already Exists")
            raise forms.ValidationError("This User Already Exists")


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = ("date_of_birth",)


class RestaurantProfileForm(forms.ModelForm):
    class Meta:
        model = RestaurantProfile
        fields = ("restaurant_address","restaurant_name",)  #'geolocation',)
        widgets = {
            "restaurant_address": forms.TextInput(
                attrs={"class": "autocomplete-items2"}
            ),
            "first_name":forms.HiddenInput(),  
            "last_name":forms.HiddenInput(),
        }
