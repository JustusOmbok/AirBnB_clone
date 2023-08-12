import unittest
from datetime import datetime, timedelta
from models.city import City
from models.base_model import Basemodel
"""
Test city module
"""

class TestCity(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures"""
        self.city = City(name='Test City', state_id='123')

    def test_attributes(self):
        """Test attributes of City instance"""
        self.assertEqual(self.city.name, 'Test City')
        self.assertEqual(self.city.state_id, '123')

    def test_inheritance(self):
        """Test inheritance from BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_str_representation(self):
        """Test __str__ representation"""
        expected_str = "[City] ({}) {}".format(self.city.id, self.city.__dict__)
        self.assertEqual(str(self.city), expected_str)

    def test_to_dict(self):
        """Test to_dict method"""
        city_dict = self.city.to_dict()
        self.assertIn('id', city_dict)
        self.assertIn('created_at', city_dict)
        self.assertIn('updated_at', city_dict)
        self.assertIn('__class__', city_dict)
        self.assertIn('name', city_dict)
        self.assertIn('state_id', city_dict)
        self.assertEqual(city_dict['name'], 'Test City')
        self.assertEqual(city_dict['state_id'], '123')

    def test_save_and_updated_at(self):
        """Test save method and updated_at attribute"""
        before_save = self.city.updated_at
        self.city.save()
        after_save = self.city.updated_at
        self.assertNotEqual(before_save, after_save)

    def test_load_from_dict(self):
        """Test loading City instance from dictionary"""
        city_dict = self.city.to_dict()
        new_city = City(**city_dict)
        self.assertEqual(self.city.id, new_city.id)
        self.assertEqual(self.city.created_at, new_city.created_at)
        self.assertEqual(self.city.updated_at, new_city.updated_at)
        self.assertEqual(self.city.name, new_city.name)
        self.assertEqual(self.city.state_id, new_city.state_id)

if __name__ == '__main__':
    unittest.main()