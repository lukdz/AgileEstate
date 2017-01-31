from django import forms

from .models import EstateModel

class EstateForm(forms.ModelForm):
    class Meta:
        model = EstateModel
        fields = ("surface", "rooms", "window_view")

    lat_site = forms.ChoiceField(widget=forms.Select, choices=[("N", "N"), ("S", "S")])
    lat_degrees = forms.IntegerField(label="Degrees of latitude", min_value=0, max_value=90)
    lat_minutes = forms.IntegerField(label="Minutes of latitude", min_value=0, max_value=59)
    lat_seconds = forms.IntegerField(label="Seconds of latitude", min_value=0, max_value=59)
    lng_site = forms.ChoiceField(widget=forms.Select, choices=[("E", "E"), ("W", "W")])
    lng_degrees = forms.IntegerField(label="Degrees of longitude", min_value=0, max_value=180)
    lng_minutes = forms.IntegerField(label="Minutes of longitude", min_value=0, max_value=59)
    lng_seconds = forms.IntegerField(label="Seconds of longitude", min_value=0, max_value=59)

    def __init__(self, user, *args, **kwargs):
        super(EstateForm, self).__init__(*args, **kwargs)
        self.user = user
        self.fields["surface"].label = "Surface"
        self.fields["rooms"].label = "Number of rooms"
        self.fields["window_view"].label = "Window view quality"

    def clean_lat_degrees(self):
        cd_lat_degrees = self.cleaned_data["lat_degrees"]
        cd_lat_site = self.cleaned_data["lat_site"]

        if cd_lat_site == "N":
            return cd_lat_degrees
        elif cd_lat_site == "S":
            return -cd_lat_degrees
        else:
            raise forms.ValidationError("Latitude direction should be N (north) or S (south).")

    def clean_lng_degrees(self):
        cd_lng_degrees = self.cleaned_data["lng_degrees"]
        cd_lng_site = self.cleaned_data["lng_site"]

        if cd_lng_site == "E":
            return cd_lng_degrees
        elif cd_lng_site == "W":
            return -cd_lng_degrees
        else:
            raise forms.ValidationError("Longitude direction should be W (west) or E (east).")
