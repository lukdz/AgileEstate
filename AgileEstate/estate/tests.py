from decimal import Decimal, getcontext

from django.test import TestCase
from .models import EstateModel

class EstateModelTestCase(TestCase):
    def __init__(self, *args, **kwargs):
        super(EstateModelTestCase, self).__init__(*args, **kwargs)
        self.model = None

    def setUp(self):
        getcontext().prec = 4
        self.model = EstateModel(longitude=180900, latitude=41869, surface=Decimal(1234.56),
                                 rooms=6, window_view=7)

    def tearDown(self):
        pass

    def test_str(self):
        result = str(self.model)
        self.assertEquals(result, "surface: 1234.56; rooms: 6; window view: wonderful; latitude: (11, 37, 49); longitude: (50, 15, 0)")

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

    def test_get_LatLng(self):
        result = self.model.get_LatLng()
        self.assertEquals(result[0], 11+37/60.0+49/3600.0)
        self.assertEquals(result[1], 50+15/60.0)

    def test_set_longitude_correct(self):
        self.model.set_longitude(52, 18, 30)
        result = self.model.longitude
        self.assertEquals(result, 188310)

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
        result = self.model.set_latitude(23, 55, 16)
        result = self.model.latitude
        self.assertEquals(result, 86116)

    def test_set_latitude_error(self):
        try:
            result = self.model.set_longitude(48, 4, 71)
        except ArithmeticError:
            pass
        except:
            self.fail()
        else:
            self.fail()

    def test_get_window_view_name(self):
        result = self.model.get_window_view_name()
        self.assertEquals(result, "wonderful")
