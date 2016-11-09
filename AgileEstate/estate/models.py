from __future__ import unicode_literals

from django.db import models

class PropertyModel(models.Model):
    country = models.TextField()
    city = models.TextField()
    surface = models.DecimalField(decimal_places=2)
    minimal_price = models.DecimalField(decimal_places=2)
    
    def save(self, *args, **kwargs):
        if self.surface <= 0:
            raise TypeError("Property surface is less than or equal to zero.")
        
        if self.minimal_price <= 0:
            raise TypeError("Property minimal_price is less than or equal to zero.")

