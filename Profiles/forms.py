from django import forms
from django.contrib.auth.models import User


class UserUpdateForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(render_value=True), required=True
    )
    password_confirmation = forms.CharField(
        widget=forms.PasswordInput(render_value=True), required=True
    )

    class Meta:
        model = User
        fields = ("username", "password", "password_confirmation")

    def clean(self):
        cleaned_data = super(UserUpdateForm, self).clean()
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")

        if password != password_confirmation:
            self.fields["password"].widget = forms.PasswordInput()
            self.fields["password_confirmation"].widget = forms.PasswordInput()

            self.add_error("password", "Must match with Password confirmation")
            self.add_error("password_confirmation", "Must match with Password")
            raise forms.ValidationError(
                "Password and Password confirmation do not match"
            )

