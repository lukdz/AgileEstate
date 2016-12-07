from __future__ import unicode_literals
from decimal import *

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Places:
    COUNTRIES = {"Afghanistan" : "AFG", "Albania" : "ALB", "Algeria" : "DZA", "Canada" : "CAN", "France" : "FRA", "Germany" : "DEU", "Hong Kong" : "HKG", "Japan" : "JPN", "North Korea" : "PRK", "Poland" : "POL", "South Korea" : "KOR", "Switzerland" : "CHE", "United Kingdom" : "GBR", "United States of America" : "USA"}

class PropertyModel(models.Model):
    VIEW_TYPES = {0 : "shit", 1 : "poor", 2 : "bad", 3 : "good", 4 : "nice", 5 : "great", 6 : "awesome", 7 : "wonderful", 8 : "breath-taking", 9 : "paradise"}
    
    country = models.TextField( list(Places.COUNTRIES.items()) )
    longitude = models.FloatField( default=0.0, validators=[ MinValueValidator(-180.0), MaxValueValidator(-180.0) ] )
    latitude = models.FloatField( default=0.0, validators=[ MinValueValidator(-90.0), MaxValueValidator(90.0) ] )
    
    surface = models.DecimalField( max_digits=902, decimal_places=4, validators=[ MinValueValidator(0.0) ] )
    num_rooms = models.PositiveIntegerField( validators=[MinValueValidator(3)] )
    window_view = models.IntegerField( list(VIEW_TYPES.items()), default=5, validators=[MinValueValidator(0), MaxValueValidator(9)] )
    
    def longitude_degrees(self):
        return int(self.longitude)
    
    def longitude_minutes(self):
        no_degrees = self.longitude-self.longitude_degrees()
        
        return int(no_degrees*60)
    
    def longitude_seconds(self):
        no_degrees = self.longitude-self.longitude_degrees()
        no_minutes = no_degrees*60-self.longitude_minutes()
        
        return int(no_minutes*60)
    
    def latitude_degrees(self):
        return int(self.latitude)
    
    def latitude_minutes(self):
        no_degrees = self.latitude-self.latitude_degrees()
        
        return int(no_degrees*60)
    
    def latitude_seconds(self):
        no_degrees = self.latitude-self.latitude_degrees()
        no_minutes = no_degrees*60-self.latitude_minutes()
        
        return int(no_minutes*60)

