from datetime import datetime
from decimal import Decimal, getcontext

from django.test import TestCase
from .models import BiddingModel

class BiddingModelTestCase(TestCase):
    def __init__(self, *args, **kwargs):
        super(EstateModelTestCase, self).__init__(*args, **kwargs)
        self.model = None

    def setUp(self):
        getcontext().prec = 2
        self.model = BiddingModel( start_time=datetime(2001, 2, 3, 4, 5, 6),
                                        end_time=datetime(2002, 10, 11, 12, 13, 14),
                                        start_price=Decimal(100.00),
                                        actual_price=Decimal(200.00) )

    def tearDown(self):
        pass

    def test_bid_open_fail_1(self):
        self.assertFalse( self.model.is_bid_open( datetime(2000, 7, 8, 9, 10, 11) ) )

    def test_bid_open_fail_2(self):
        self.assertFalse( self.model.is_bid_open( datetime(2003, 7, 8, 9, 10, 11) ) )

    def test_bid_open_correct(self):
        self.assertTrue( self.model.is_bid_open( datetime(2001, 7, 8, 9, 10, 11) ) )

    def test_check_new_actual_price_error_1(self):
        try:
            result = self.model.check_new_actual_price( Decimal(210.00),
                                                             datetime(2003, 7, 8, 9, 10, 11), )
        except SystemError:
            pass
        except:
            self.fail()
        else:
            self.fail()

    def test_check_new_actual_price_error_2(self):
        try:
            result = self.model.check_new_actual_price( Decimal(190.00),
                                                             datetime(2001, 7, 8, 9, 10, 11) )
        except AttributeError:
            pass
        except:
            self.fail()
        else:
            self.fail()

    def test_check_new_actual_price_correct(self):
        result = self.model.check_new_actual_price( Decimal(210.00),
                                                         datetime(2001, 7, 8, 9, 10, 11) )
        self.assertTrue(result)
