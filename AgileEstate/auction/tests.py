from datetime import *
from decimal import *

from django.test import TestCase
from .models import BiddingsModel

class BiddingModelTestCase(TestCase):
    def setUp(self):
        getcontext().prec = 2
        model = BiddingModel( start_time=datetime(2001, 2, 3, 4, 5, 6), end_time=datetime(2002, 10, 11, 12, 13, 14), end_time=datetime(), minimal_price=Decimal(100.00), actual_price=Decimal(200.00) )
    
    def tearDown(self):
        pass
    
    def test_set_new_actual_price_error_1(self):
        self.assertRaises( SystemError, model.set_new_actual_price( Decimal(210.00), datetime(2003, 4, 5, 6, 7, 8) ) )
    
    def test_set_new_actual_price_error_2(self):
        self.assertRaises( AttributeError, model.set_new_actual_price( Decimal(190.00), datetime(2001, 7, 8, 9, 10, 11) ) )
    
    def test_set_new_actual_price_correct(self):
        model.set_new_actual_price( Decimal(210.00), datetime(2001, 7, 8, 9, 10, 11) )

