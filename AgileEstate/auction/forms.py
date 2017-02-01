from django import forms
from datetime import timedelta

from .models import BiddingModel
from estate.models import EstateModel

class BiddingForm(forms.ModelForm):
    class Meta:
        model = BiddingModel
        fields = ("start_time", "end_time", "start_price")

    def __init__(self, user, *args, **kwargs):
        super(BiddingForm, self).__init__(*args, **kwargs)
        self.user = user
        self.fields["start_time"].label = "Beginning time of auction"
        self.fields["end_time"].label = "Ending time of auction"
        self.fields["start_price"].label = "Starting price"
        user_estates = EstateModel.objects.filter(owner_key=user.id) if not self.user.is_anonymous else EstateModel.objects.filter(owner_key=3)
        estate_choice = list(map(lambda obj: (obj.id, str(obj)), user_estates))
        self.fields["estate"] = forms.ChoiceField(widget=forms.Select, choices=estate_choice)
        self.fields["estate"].label = "Property"

    def clean_end_time(self):
        cd_end_time = self.cleaned_data["end_time"]
        cd_start_time = self.cleaned_data["start_time"]

        if cd_end_time-cd_start_time < timedelta(1):
            raise forms.ValidationError("Bidding duration time must come to at least 24 hours.")

        return cd_end_time
