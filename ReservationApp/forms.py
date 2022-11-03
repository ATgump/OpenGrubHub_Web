from django import forms
from .models import ReservationModel

TIME_CHOICES = [
                ("5:00 PM","5:00 PM"),
                ("5:15 PM","5:15 PM"),
                ("5:30 PM","5:30 PM"),
                ("5:45 PM","5:45 PM"),
                ("6:00 PM","6:00 PM"),
                ("6:15 PM","6:15 PM"),
                ("6:30 PM","6:30 PM"),
                ("6:45 PM","6:45 PM"),
                ("7:00 PM","7:00 PM"),
                ("7:15 PM","7:15 PM"),
                ("7:30 PM","7:30 PM"),
                ("7:45 PM","7:45 PM"),
                ("8:00 PM","8:00 PM"),
                ("8:15 PM","8:15 PM"),
                ("8:30 PM","8:30 PM"),
                ("8:45 PM","8:45 PM"),
                ("9:00 PM","9:00 PM"),
]


class ReservationForm(forms.ModelForm):
    class Meta:
        model = ReservationModel
        fields = (
            "first_name",
            "last_name",
            "email",
            "time",
            "date",
            "table_size",
            "phone_number",
            "high_seat",
        )
