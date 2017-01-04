from __future__ import unicode_literals
from decimal import Decimal

from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator

class BiddingModel(models.Model):
    property_key = models.OneToOneField("estate.PropertyModel", on_delete=models.CASCADE)
    owner_key = models.OneToOneField("users.UserProfile", default=0, on_delete=models.CASCADE,
                                     related_name="%(class)s_owner_user")
    winner_key = models.OneToOneField("users.UserProfile", default=0, on_delete=models.CASCADE,
                                      related_name="%(class)s_winner_user")

    start_time = models.DateTimeField(default=timezone.now())
    end_time = models.DateTimeField( default=timezone.now(),
                                     validators=[ MinValueValidator(start_time) ] )
    start_price = models.DecimalField( max_digits=902, decimal_places=2, default=Decimal(0.01),
                                       validators=[ MinValueValidator( Decimal(0.01) ) ] )
    actual_price = models.DecimalField( max_digits=902, decimal_places=2, default=start_price,
                                        blank=True, validators=[ MinValueValidator(start_price) ] )

    def set_new_actual_price(self, new_price, time, testing=False):
        if not self.is_bid_open(time):
            raise SystemError("Cannot bid when auction is not open.")

        if new_price <= self.actual_price:
            raise AttributeError("New price is less than actual price.")

        if not testing:
            self.actual_price = new_price

    def is_bid_open(self, time):
        return self.start_time <= time <= self.end_time
