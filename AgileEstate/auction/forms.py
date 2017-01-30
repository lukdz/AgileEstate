from django import forms

from .models import BiddingModel

class BiddingForm(forms.ModelForm):
    class Meta:
        model = BiddingModel
        fields = ("start_time", "end_time", "start_price")

    def __init__(self, user, *args, **kwargs):
        super(BiddingForm, self).__init__(*args, **kwargs)
        self.user = user
