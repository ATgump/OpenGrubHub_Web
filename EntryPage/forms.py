from django import forms
from django.db import models,transaction
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from Profiles.models import CustomerProfile,RestaurantProfile,User
from django.contrib.auth import authenticate


class UserLoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user) -> None:
        if not user.is_active:
            raise forms.ValidationError(("This account is inactive."),code='inactive',)
        return super().confirm_login_allowed(user)



### Update these forms for the user create Page 
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(render_value=True), required=True)
    password_confirmation = forms.CharField(widget=forms.PasswordInput(render_value=True), required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password_confirmation')

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")
        username = cleaned_data.get("username")
        if password != password_confirmation:
            self.fields['password'].widget = forms.PasswordInput()
            self.fields['password_confirmation'].widget = forms.PasswordInput()

            self.add_error('password', "Must match with Password confirmation")
            self.add_error('password_confirmation', "Must match with Password")
            raise forms.ValidationError(
                "Password and Password confirmation do not match"
            )
        elif User.objects.filter(username=username).exists():
            self.fields['username'].widget = forms.TextInput()
            self.add_error('username',"User Already Exists")
            raise forms.ValidationError(
                "This User Already Exists"
            )


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model=CustomerProfile
        fields=('birth_date',)
class RestaurantProfileForm(forms.ModelForm):
    class Meta:
        model=RestaurantProfile
        fields=('address',)
# class CustomerProfileForm(UserCreationForm):
#     birth_date = forms.DateField()
#     class Meta(UserCreationForm.Meta):
#         model= User
#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.is_customer = True
#         user.save()
#         customer = CustomerProfile.objects.create(user=user)
#         customer.birth_date.add(*self.cleaned_data.get('birth_date'))


# class RestaurantProfileForm(UserCreationForm):
#     address = forms.CharField(max_length=140)
#     class Meta(UserCreationForm.Meta):
#         model= User
#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.is_customer = True
#         user.save()
#         restaurant = RestaurantProfile.objects.create(user=user)
#         restaurant.address.add(*self.cleaned_data.get('address'))
