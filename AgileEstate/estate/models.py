from __future__ import unicode_literals
from decimal import Decimal

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Places:
    COUNTRIES = {"Afghanistan" : "AFG", "Albania" : "ALB", "Algeria" : "DZA", "Canada" : "CAN",
                 "France" : "FRA", "Germany" : "DEU", "Hong Kong" : "HKG", "Japan" : "JPN",
                 "North Korea" : "PRK", "Poland" : "POL", "South Korea" : "KOR",
                 "Switzerland" : "CHE", "United Kingdom" : "GBR",
                 "United States of America" : "USA"}

class EstateModel(models.Model):
    VIEW_TYPES = {"shit" : 0, "poor" : 1, "bad" : 2, "good" : 3, "nice" : 4, "great" : 5,
                  "awesome" : 6, "wonderful" : 7, "breath-taking" : 8, "paradise" : 9}

    country = models.TextField( choices=tuple(Places.COUNTRIES.items()) )
    longitude = models.IntegerField(default=0,
                                    validators=[MinValueValidator(-648000),
                                                MaxValueValidator(648000)])
    latitude = models.IntegerField(default=0,
                                   validators=[MinValueValidator(-324000),
                                               MaxValueValidator(324000)])

    surface = models.DecimalField(max_digits=904, decimal_places=4, default=Decimal(0.0),
                                  validators=[MinValueValidator( Decimal(0.0) )])
    rooms = models.PositiveIntegerField(validators=[MinValueValidator(3)])
    window_view = models.PositiveSmallIntegerField(choices=tuple(VIEW_TYPES.items()), default=5,
                                                   validators=[MinValueValidator(0),
                                                               MaxValueValidator(9)])

    def get_longitude(self):
        return self.longitude//3600, (self.longitude//60)%60, self.longitude%60

    def count_longitude(self, deg, min, sec):
        if -180 <= deg <= 180 and 0 <= min <= 60 and 0 <= sec <= 60:
            return deg*3600+min*60+sec
        else:
            raise ArithmeticError("Incorrect values of longitude coordinates.")

    def get_latitude(self):
        return (self.latitude//3600, (self.latitude//60)%60, self.latitude%60)

    def count_latitude(self, deg, min, sec):
        if -90 <= deg <= 90 and 0 <= min <= 60 and 0 <= sec <= 60:
            return deg*3600+min*60+sec
        else:
            raise ArithmeticError("Incorrect values of latitude coordinates.")

