from django import forms
from .models import ReservationModel
import datetime
import phonenumbers
TIME_CHOICES = [
                (datetime.time(5),"5:00 PM"),
                (datetime.time(5,15),"5:15 PM"),
                (datetime.time(5,30),"5:30 PM"),
                (datetime.time(5,45),"5:45 PM"),
                (datetime.time(6),"6:00 PM"),
                (datetime.time(6,15),"6:15 PM"),
                (datetime.time(6,30),"6:30 PM"),
                (datetime.time(6,45),"6:45 PM"),
                (datetime.time(7),"7:00 PM"),
                (datetime.time(7,15),"7:15 PM"),
                (datetime.time(7,30),"7:30 PM"),
                (datetime.time(7,45),"7:45 PM"),
                (datetime.time(8),"8:00 PM"),
                (datetime.time(8,15),"8:15 PM"),
                (datetime.time(8,30),"8:30 PM"),
                (datetime.time(8,45),"8:45 PM"),
                (datetime.time(9),"9:00 PM"),
]
TABLE_SIZES = [
                ("2",2),
                ("3",3),
                ("4",4),
                ("5",5),
                ("6",6),
                ("7",7),
                ("8",8),
                ("9",9),
                ("10",10),

]

class ReservationForm(forms.ModelForm):
    class Meta:
        valid_time_formats = ['%I:%M %p']
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
        widgets = {
            "time":forms.Select(choices=TIME_CHOICES,attrs={"valid_formats":valid_time_formats}),
            "table_size":forms.Select(choices=TABLE_SIZES),
        }
    def clean_phoneNumber(self):
        phone_number = self.cleaned_data['phone_number']
        # Replace 'US' with whatever type of number it is //// for now just support US numbers
        # See https://github.com/daviddrysdale/python-phonenumbers 
        parsed_number = phonenumbers.parse(phone_number, 'US')
        return phonenumbers.format_number(
            parsed_number,
            phonenumbers.PhoneNumberFormat.E164,
        )
