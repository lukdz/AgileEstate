from decimal import *

from django.test import TestCase
from .models import PropertyModel

class PropertyModelTestCase(TestCase):
    def setUp(self):
        getcontext().prec = 2
        model = BiddingModel( country="Poland", longitude=50.25, latitude=10.2, minimal_price=Decimal(100.00), actual_price=Decimal(200.00) )
    
    def tearDown(self):
        pass
    
    
