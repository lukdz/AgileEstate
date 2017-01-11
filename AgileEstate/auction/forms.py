from django import forms

from .models import BiddingModel

class BiddingForm(forms.ModelForm):
    class Meta:
        model = BiddingModel
        fields = ("start_time", "end_time", "start_price")