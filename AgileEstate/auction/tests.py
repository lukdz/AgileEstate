from datetime import *
from decimal import *

from django.test import TestCase
from .models import *

class BiddingModelTestCase(TestCase):
    def setUp(self):
        getcontext().prec = 2
        self.model_test = BiddingModel( start_time=datetime(2001, 2, 3, 4, 5, 6), end_time=datetime(2002, 10, 11, 12, 13, 14), minimal_price=Decimal(100.00), actual_price=Decimal(200.00) )

    def tearDown(self):
        pass

    def test_bid_open_fail_1(self):
        self.assertFalse( self.model_test.is_bid_open( datetime(2000, 7, 8, 9, 10, 11) ) )

    def test_bid_open_fail_2(self):
        self.assertFalse( self.model_test.is_bid_open( datetime(2003, 7, 8, 9, 10, 11) ) )

    def test_bid_open_correct(self):
        self.assertTrue( self.model_test.is_bid_open( datetime(2001, 7, 8, 9, 10, 11) ) )

    def test_set_new_actual_price_error_1(self):
        try:
            self.model_test.set_new_actual_price( Decimal(210.00), datetime(2003, 7, 8, 9, 10, 11) )
        except SystemError:
            pass
        except:
            self.fail()
        else:
            self.fail()

    def test_set_new_actual_price_error_2(self):
        try:
            self.model_test.set_new_actual_price( Decimal(190.00), datetime(2001, 7, 8, 9, 10, 11) )
        except AttributeError:
            pass
        except:
            self.fail()
        else:
            self.fail()

    def test_set_new_actual_price_correct(self):
        self.model_test.set_new_actual_price( Decimal(210.00), datetime(2001, 7, 8, 9, 10, 11) )

