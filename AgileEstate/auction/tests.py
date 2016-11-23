from django.test import TestCase

from .models import BiddingsModel

from decimal import *

class BiddingModelTestCase(TestCase):
    def setUp(self):
        getcontext().prec = 2
        model = BiddingModel( minimal_price=Decimal(100.00), actual_price=Decimal(200.00) )
    
    def tearDown(self):
        pass
    
    def test_set_new_actual_price_error(self):
        self.assertRaises(AttributeError, model.set_new_actual_price( Decimal(190.00) ))
    
    def test_set_new_actual_price_correct(self):
        model.set_new_actual_price( Decimal(190.00) )

