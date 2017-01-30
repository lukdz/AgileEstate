from django import forms

from .models import EstateModel

class EstateForm(forms.ModelForm):
    class Meta:
        model = EstateModel
        fields = ("surface", "rooms", "window_view")

    lng_degrees = forms.IntegerField(label="degrees of longitude", min_value=-179, max_value=180)
    lng_minutes = forms.IntegerField(label="minutes of longitude", min_value=0, max_value=59)
    lng_seconds = forms.IntegerField(label="seconds of longitude", min_value=0, max_value=59)
    lat_degrees = forms.IntegerField(label="degrees of latitude", min_value=-90, max_value=90)
    lat_minutes = forms.IntegerField(label="minutes of latitude", min_value=0, max_value=59)
    lat_seconds = forms.IntegerField(label="seconds of latitude", min_value=0, max_value=59)

    def __init__(self, user, *args, **kwargs):
        super(EstateForm, self).__init__(*args, **kwargs)
        self.user = user
        self.fields["surface"].label = "surface [m^2]"
