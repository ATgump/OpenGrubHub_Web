from django import forms
from .models import ReservationModel
import datetime
import phonenumbers
## TIME choices for selection
TIME_CHOICES = [
                (datetime.time(17),"5:00 PM"),
                (datetime.time(17,15),"5:15 PM"),
                (datetime.time(17,30),"5:30 PM"),
                (datetime.time(17,45),"5:45 PM"),
                (datetime.time(18),"6:00 PM"),
                (datetime.time(18,15),"6:15 PM"),
                (datetime.time(18,30),"6:30 PM"),
                (datetime.time(18,45),"6:45 PM"),
                (datetime.time(19),"7:00 PM"),
                (datetime.time(19,15),"7:15 PM"),
                (datetime.time(19,30),"7:30 PM"),
                (datetime.time(19,45),"7:45 PM"),
                (datetime.time(20),"8:00 PM"),
                (datetime.time(20,15),"8:15 PM"),
                (datetime.time(20,30),"8:30 PM"),
                (datetime.time(20,45),"8:45 PM"),
                (datetime.time(21),"9:00 PM"),
]
## Table sizes for selection
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

## Form for reservation
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
        exclude = ("restaurant","customer",)
        widgets = {
           
            "time":forms.Select(choices=TIME_CHOICES,attrs={"valid_formats":valid_time_formats}), ## widgets for selection form field
            "table_size":forms.Select(choices=TABLE_SIZES),
        }
    ## clean phone number (unfortunatly did not have as much time to work on phone number field as I would have liked)
    def clean_phoneNumber(self):
        phone_number = self.cleaned_data['phone_number']
        parsed_number = phonenumbers.parse(phone_number, 'US')
        return phonenumbers.format_number(
            parsed_number,
            phonenumbers.PhoneNumberFormat.E164,
        )
