from django import forms

from .models import PropertyModel

class PropertyForm(forms.ModelForm):
    class Meta:
        model = PropertyModel
        fields = ("country", "surface", "rooms", "window_view")

    lng_degrees = forms.IntegerField(label="degrees of longitude")
    lng_minutes = forms.IntegerField(label="minutess of longitude")
    lng_seconds = forms.IntegerField(label="seconds of longitude")
    lat_degrees = forms.IntegerField(label="degrees of latitude")
    lat_minutes = forms.IntegerField(label="minutess of latitude")
    lat_seconds = forms.IntegerField(label="seconds of latitude")
