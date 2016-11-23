from django.test import TestCase

from .models import PropertyModel

from decimal import *

class PropertyModelTestCase(TestCase):
    def setUp(self):
        getcontext().prec = 2
        model = BiddingModel( minimal_price=Decimal(100.00), actual_price=Decimal(200.00) )
    
    def tearDown(self):
        pass
    
