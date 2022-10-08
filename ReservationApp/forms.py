from django import forms
from .models import ReservationModel


class ReservationForm(forms.ModelForm):
    class Meta:
        model = ReservationModel
        fields = (
            "time",
            "date",
            "number_of_customers",
        )

    # def clean(self):
    #     cleaned_data = super(UserUpdateForm, self).clean()
    #     password = cleaned_data.get("password")
    #     password_confirmation = cleaned_data.get("password_confirmation")

    #     if password != password_confirmation:
    #         self.fields['password'].widget = forms.PasswordInput()
    #         self.fields['password_confirmation'].widget = forms.PasswordInput()

    #         self.add_error('password', "Must match with Password confirmation")
    #         self.add_error('password_confirmation', "Must match with Password")
    #         raise forms.ValidationError(
    #             "Password and Password confirmation do not match"
    #         )
