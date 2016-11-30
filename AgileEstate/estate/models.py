from __future__ import unicode_literals
from decimal import *

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Places:
    COUNTRIES = {"Afghanistan" : "AFG", "Albania" : "ALB", "Algeria" : "DZA", "Canada" : "CAN", "France" : "FRA", "Germany" : "DEU", "Hong Kong" : "HKG", "Japan" : "JPN", "North Korea" : "PRK", "Poland" : "POL", "South Korea" : "KOR", "Switzerland" : "CHE", "United Kingdom" : "GBR", "United States of America" : "USA"}

class PropertyModel(models.Model):
    VIEW_TYPES = {"0" : "shit", "1" : "poor", "2" : "bad", "3" : "good", "4" : "nice", "5" : "great", "6" : "awesome", "7" : "wonderful", "8" : "breath-taking", "9" : "paradise"}
    
    country = models.TextField( list(Places.COUNTRIES.items()) )
    place = models.TextField()
    
    surface = models.DecimalField( max_digits=1002, decimal_places=2, validators=[ MinValueValidator(0.0) ] )
    num_rooms = models.PositiveIntegerField( validators=[MinValueValidator(3)] )
    window_view = models.IntegerField( list(VIEW_TYPES.items()), validators=[MinValueValidator(0), MaxValueValidator(9)] )

