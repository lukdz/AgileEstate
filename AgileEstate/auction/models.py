from __future__ import unicode_literals
from datetime import *
from decimal import *

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.timezone import utc

class BiddingModel(models.Model):
    property_key = models.OneToOneField('estate.PropertyModel', models.CASCADE)
    owner_key = models.OneToOneField('users.CustomUser', models.CASCADE)
    #winner_key = models.OneToOneField('users.CustomUser', models.CASCADE)
    
    start_time = models.DateTimeField( default=datetime.utcnow().replace(tzinfo=utc) )
    end_time = models.DateTimeField( default=datetime.utcnow().replace(tzinfo=utc), validators=[ MinValueValidator(start_time) ] )
    minimal_price = models.DecimalField( max_digits=902, decimal_places=2, default=0.0, validators=[ MinValueValidator(0.0) ] )
    actual_price = models.DecimalField( max_digits=902, decimal_places=2, default=minimal_price, validators=[ MinValueValidator(minimal_price) ] )
    
    def set_new_actual_price(self, new_price, time):
        if not self.is_bid_open(time):
            raise SystemError("Cannot bid when auction is not open.")
        
        if new_price <= self.actual_price:
            raise AttributeError("New price is less than actual price.")
    
        self.actual_price = new_price
    
    def is_bid_open(self, time):
        return self.start_time <= time <= self.end_time
