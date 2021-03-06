from __future__ import unicode_literals
from decimal import Decimal

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class EstateModel(models.Model):
    _VIEWS = {0 : "shit", 1 : "poor", 2 : "bad", 3 : "good", 4 : "nice", 5 : "great",
              6 : "awesome", 7 : "wonderful", 8 : "breath-taking", 9 : "paradise"}

    owner_key = models.ForeignKey("users.UserProfile", default=3, on_delete=models.CASCADE,
                                  related_name="%(class)s_owner_user")
    longitude = models.IntegerField(default=0,
                                    validators=[MinValueValidator(-648000),
                                                MaxValueValidator(648000)])
    latitude = models.IntegerField(default=0,
                                   validators=[MinValueValidator(-324000),
                                               MaxValueValidator(324000)])

    surface = models.DecimalField(max_digits=904, decimal_places=4, default=Decimal(1.0),
                                  validators=[MinValueValidator( Decimal(1.0) )])
    rooms = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    window_view = models.PositiveIntegerField(choices=sorted(_VIEWS.items()),
                                              validators=[MinValueValidator(0),
                                                          MaxValueValidator(9)])

    def __str__(self):
        return "surface: "+str(float(self.surface))+"; rooms: "+str(self.rooms)+ \
               "; window view: "+self._VIEWS[self.window_view]+"; latitude: "+ \
               str(self.get_latitude())+"; longitude: "+str(self.get_longitude())

    def get_longitude(self):
        return self.longitude//3600, (self.longitude//60)%60, self.longitude%60

    def set_longitude(self, degs, mins, secs):
        if -180 <= degs <= 180 and 0 <= mins <= 60 and 0 <= secs <= 60:
            self.longitude = degs*3600+mins*60+secs
        else:
            raise ArithmeticError("Incorrect values of longitude coordinates.")

    def get_latitude(self):
        return self.latitude//3600, (self.latitude//60)%60, self.latitude%60

    def set_latitude(self, degs, mins, secs):
        if -90 <= degs <= 90 and 0 <= mins <= 60 and 0 <= secs <= 60:
            self.latitude =  degs*3600+mins*60+secs
        else:
            raise ArithmeticError("Incorrect values of latitude coordinates.")

    def get_LatLng(self):
        Lat_deg, Lat_min, Lat_sec = self.get_latitude()
        Lng_deg, Lng_min, Lng_sec = self.get_longitude()

        return Lat_deg+Lat_min/60.0+Lat_sec/3600.0, Lng_deg+Lng_min/60.0+Lng_sec/3600.0

    def get_window_view_name(self):
        return self._VIEWS[self.window_view]
