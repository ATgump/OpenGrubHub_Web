from django import forms
from django.contrib.auth.forms import AuthenticationForm
from Profiles.models import CustomerProfile, RestaurantProfile, User

## Form for user Login/authentication, most functionality built in with django
class UserLoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user) -> None:
        if not user.is_active:
            raise forms.ValidationError(
                ("This account is inactive."),
                code="inactive",
            )
        return super().confirm_login_allowed(user)

## Form for creating a base user
class UserForm(forms.ModelForm):
    ## set password field widgets
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
        ## make sure passwords match
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
        ## check if the user already exists
        elif User.objects.filter(email=email).exists():
            self.fields["email"].widget = forms.TextInput()
            self.add_error("email", "User Already Exists")
            raise forms.ValidationError("This User Already Exists")


## Customer Profile Form (Created during customer creation)
class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = ("date_of_birth",)


## Restaurant Profile Form (Created during restaurant creation)
class RestaurantProfileForm(forms.ModelForm):
    class Meta:
        model = RestaurantProfile
        fields = ("restaurant_address","restaurant_name","lat","long")
        widgets = {
            "restaurant_address": forms.TextInput(
                attrs={"class": "autocomplete-it"}
            ),
            "first_name":forms.HiddenInput(),   ## Hidden inputs for fields irrelevant to restuarant as well as the lat long we want for the 50 mi radius checking
            "last_name":forms.HiddenInput(),
            "lat":forms.HiddenInput(),  
            "long":forms.HiddenInput(),
        }
