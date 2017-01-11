from django import forms

from .models import EstateModel

class EstateForm(forms.ModelForm):
    class Meta:
        model = EstateModel
        fields = ("country", "surface", "rooms", "window_view")

    lng_degrees = forms.IntegerField(label="degrees of longitude")
    lng_minutes = forms.IntegerField(label="minutess of longitude")
    lng_seconds = forms.IntegerField(label="seconds of longitude")
    lat_degrees = forms.IntegerField(label="degrees of latitude")
    lat_minutes = forms.IntegerField(label="minutess of latitude")
    lat_seconds = forms.IntegerField(label="seconds of latitude")

    def clean_lng_degrees(self):
        lng_deg = self.cleaned_data["lng_degrees"]

        if abs(lng_deg) > 180:
            raise forms.ValidationError("Incorrect value of longitude in degrees")

        return lng_deg

    def clean_lat_degrees(self):
        lat_deg = self.cleaned_data["lat_degrees"]

        if abs(lat_deg) > 90:
            raise forms.ValidationError("Incorrect value of longitude in degrees")

        return lat_deg

    def clean_lng_minutes(self):
        return self._clean_minutes("lng_minutes")

    def clean_lat_minutes(self):
        return self._clean_minutes("lat_minutes")

    def clean_lng_seconds(self):
        return self._clean_minutes("lng_seconds")

    def clean_lat_seconds(self):
        return self._clean_minutes("lat_seconds")

    def _clean_minutes(self, fieldname):
        mins = self.cleaned_data[fieldname]

        if mins < 0 or mins >= 60:
            raise forms.ValidationError("Incorrect value of minutes")

        return mins

    def _clean_seconds(self, fieldname):
        secs = self.cleaned_data[fieldname]

        if secs < 0 or secs >= 60:
            raise forms.ValidationError("Incorrect value of seconds")

        return secs
