from django.db import models

from decimal import *

class BiddingModel(models.Model):
    property_key = models.ForeignKey('PropertyModel', models.CASCADE)
    owner_key = models.ForeignKey('Users', models.CASCADE)
    
    minimal_price = models.DecimalField(max_digits=1002, decimal_places=2, default=0.0, validators=[ MinValueValidator(0.0) ] )
    actual_price = models.DecimalField(max_digits=1002, decimal_places=2, default=minimal_price, validators=[ MinValueValidator(minimal_price) ] )
    
    def set_new_actual_price(self, new_price):
        if new_price <= self.actual_price:
            raise AttributeError("New price is less than actual price.")
        
        self.self.actual_price = new_price
