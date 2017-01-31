from django import forms
from datetime import timedelta

from .models import BiddingModel

class BiddingForm(forms.ModelForm):
    class Meta:
        model = BiddingModel
        fields = ("start_time", "end_time", "start_price")

    def __init__(self, user, *args, **kwargs):
        super(BiddingForm, self).__init__(*args, **kwargs)
        self.user = user
        self.fields["start_time"].label = "beginning time of auction"
        self.fields["end_time"].label = "ending time of auction"
        self.fields["start_price"].label = "start price"

    def clean_end_time(self):
        cd_end_time = self.cleaned_data["end_time"]
        cd_start_time = self.cleaned_data["start_time"]

        if cd_end_time-cd_start_time < timedelta(1):
            raise forms.ValidationError("Bidding duration time must come to at least 24 hours.")

        return cd_end_time
