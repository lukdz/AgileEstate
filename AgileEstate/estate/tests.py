from decimal import *

from django.test import TestCase
from .models import PropertyModel

class PropertyModelTestCase(TestCase):
    def setUp(self):
        getcontext().prec = 4
        self.model = PropertyModel( country="Poland", longitude=180900, latitude=41869, surface=Decimal(1234.56), rooms = 6, window_view="7" )

    def tearDown(self):
        pass

    def test_get_longitude(self):
        result = self.model.get_longitude()
        self.assertEquals(result[0], 50)
        self.assertEquals(result[1], 15)
        self.assertEquals(result[2], 0)

    def test_get_latitude(self):
        result = self.model.get_latitude()
        self.assertEquals(result[0], 11)
        self.assertEquals(result[1], 37)
        self.assertEquals(result[2], 49)

    def test_set_longitude_correct(self):
        self.model.set_longitude(52, 18, 30)
        self.assertEquals(self.model.longitude, 188310)

    def test_set_longitude_error(self):
        try:
            self.model.set_longitude(13, 67, 44)
        except ArithmeticError:
            pass
        except:
            self.fail()
        else:
            self.fail()

    def test_set_latitude_correct(self):
        self.model.set_latitude(23, 55, 16)
        self.assertEquals(self.model.latitude, 86116)

    def test_set_latitude_error(self):
        try:
            self.model.set_longitude(48, 4, 71)
        except ArithmeticError:
            pass
        except:
            self.fail()
        else:
            self.fail()
