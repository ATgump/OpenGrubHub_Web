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
            "username",
            "password",
            "password_confirmation",
        )
        widgets = {
            "username": forms.TextInput(attrs={"class": "autocomplete-items2"})
            # 'password':forms.PasswordInput(attrs={"class":"input-field"}),
            # 'password_confirmation':forms.PasswordInput(attrs={"class":"input-field"})
        }

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")
        username = cleaned_data.get("username")
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
        elif User.objects.filter(username=username).exists():
            self.fields["username"].widget = forms.TextInput()
            self.add_error("username", "User Already Exists")
            raise forms.ValidationError("This User Already Exists")


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = ("birth_date",)


class RestaurantProfileForm(forms.ModelForm):
    class Meta:
        model = RestaurantProfile
        fields = ("address",)  #'geolocation',)
        widgets = {
            "address": forms.TextInput(
                attrs={"class": "autocomplete-items2"}
            ),  # attrs={'onkeyup':'test()'}
            # 'address':map_widgets.GoogleMapsAddressWidget(attrs=
            # {'data-autocomplete-options': json.dumps({'types':['geocode','establishment'],'componentRestrictions':{'country':'us'}})}
            # ),
            #'geolocation':forms.HiddenInput(),
        }

    # def test():
    #     "<h1> THis is a test of test </h1>"
    # def get_autocomplete_suggestions(location,session_token):
    #     url = f"https://maps.googleapis.com/maps/api/place/autocomplete/json?"
    #     payload={
    #         'key':settings.GOOGLE_MAPS_API_KEY,
    #         'location':location
    #     }
    #     headers = {}
    #     s = requests.Session()
    #     #response = requests
    #     response = requests.Request("GET", url, headers=headers, data=payload)
    #     print(response.url)
