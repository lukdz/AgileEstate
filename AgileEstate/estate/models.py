from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinValueValidator

from decimal import *

class Places:
    countries_map = {"CA" : "Canada", "CH" : "Switzerland", "DE" : "Germany", "FR" : "France", "GB" : "United Kingdom", "HK" : "Hong Kong", "JP" : "Japan", "PL" : "Poland", "US" : "United States of America"}
    cities_map = {"BER" : "Berlin", "LON": "London", "MTL" : "Montreal", "NYK" : "New York", "PAR" : "Paris", "TOK" : "Tokio", "WDC" : "Washington DC", "WRO" : "Wroclaw", "ZUR" : "Zurich"}

class PropertyModel(models.Model):
    VIEW_TYPES = [("0", "shit"), ("1", ""), ("2", ""), ("3", ""), ("4", ""), ("5", ""), ("6", ""), ("7", "wonderful"), ("8", ""), ("9", "paradise")]
    
    country = models.TextField( list(Places.countries_map.items()) )
    city = models.TextField( list(Places.cities_map.items()) )
    
    surface = models.DecimalField( max_digits=1002, decimal_places=2, validators=[ MinValueValidator(0.0) ] )
    num_rooms = models.PositiveIntegerField( validators=[MinValueValidator(3)] )
    window_view = models.IntegerField()

