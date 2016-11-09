from django.test import TestCase

from .models import PropertyModel

class PropertyModelTestCase(TestCase):
    def setUp(self):
        model = PropertyModel(country="Country", city="City")
    
    def tearDown(self):
        pass
    
    def test_save_when_surface_is_less_than_zero(self):
        model.surface = -123.45
        self.assertRaises(TypeError, model.save())
    
    def test_save_when_surface_equals_zero(self):
        model.surface = 0.0
        self.assertRaises(TypeError, model.save())
        
    def test_save_when_minimal_price_is_less_than_zero(self):
        model.minimal_price = -123.45
        self.assertRaises(TypeError, model.save())
    
    def test_save_when_minimal_price_equals_zero(self):
        model.minimal_price = 0.0
        self.assertRaises(TypeError, model.save())

