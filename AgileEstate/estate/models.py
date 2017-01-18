from __future__ import unicode_literals
from decimal import Decimal

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Places:
    COUNTRIES = {"AFG" : "Afghanistan", "ALB" : "Albania", "CAN" : "Canada", "CHE" : "Switzerland",
                 "DEU" : "Germany", "DZA" : "Algeria", "FRA" : "France", "GBR" : "United Kingdom",
                 "HKG" : "Hong Kong", "JPN" : "Japan", "KOR" : "South Korea", "POL" : "Poland",
                 "PRK" : "North Korea", "USA" : "United States of America"}

class EstateModel(models.Model):
    _BY_SECOND = lambda pair: (pair[1], pair[0])
    _VIEWS = {0 : "shit", 1 : "poor", 2 : "bad", 3 : "good", 4 : "nice", 5 : "great",
              6 : "awesome", 7 : "wonderful", 8 : "breath-taking", 9 : "paradise"}

    owner_key = models.OneToOneField("users.UserProfile", default=0, on_delete=models.CASCADE,
                                     related_name="%(class)s_owner_user")
    country = models.CharField( max_length=1,
                                choices=sorted(Places.COUNTRIES.items(), key=_BY_SECOND) )
    longitude = models.IntegerField(default=0,
                                    validators=[MinValueValidator(-648000),
                                                MaxValueValidator(648000)])
    latitude = models.IntegerField(default=0,
                                   validators=[MinValueValidator(-324000),
                                               MaxValueValidator(324000)])

    surface = models.DecimalField(max_digits=904, decimal_places=4, default=Decimal(0.0),
                                  validators=[MinValueValidator( Decimal(0.0) )])
    rooms = models.PositiveIntegerField(validators=[MinValueValidator(3)])
    window_view = models.CharField(max_length=1, choices=sorted(_VIEWS.items(), key=_BY_SECOND),
                                   validators=[MinValueValidator(0), MaxValueValidator(9)])

    def get_longitude(self):
        return self.longitude//3600, (self.longitude//60)%60, self.longitude%60

    def count_longitude(self, degs, mins, secs):
        if -180 <= degs <= 180 and 0 <= mins <= 60 and 0 <= secs <= 60:
            return degs*3600+mins*60+secs
        else:
            raise ArithmeticError("Incorrect values of longitude coordinates.")

    def get_latitude(self, latitude):
        return self.latitude//3600, (self.latitude//60)%60, self.latitude%60

    def count_latitude(self, degs, mins, secs):
        if -90 <= degs <= 90 and 0 <= mins <= 60 and 0 <= secs <= 60:
            return degs*3600+mins*60+secs
        else:
            raise ArithmeticError("Incorrect values of latitude coordinates.")

