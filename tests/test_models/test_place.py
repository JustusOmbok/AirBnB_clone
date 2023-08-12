import unittest
from datetime import datetime
from models.place import Place

class TestPlace(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures"""
        self.place = Place(
            city='Test City',
            user_id='test_user',
            name='Test Place',
            description='Test description',
            number_rooms=2,
            number_bathrooms=1,
            max_guest=4,
            price_by_night=100,
            latitude=123.456,
            longitude=-78.901,
            amenity_ids=[1, 2, 3]
        )

    def test_attributes(self):
        """Test attributes of Place instance"""
        self.assertEqual(self.place.city, 'Test City')
        self.assertEqual(self.place.user_id, 'test_user')
        self.assertEqual(self.place.name, 'Test Place')
        self.assertEqual(self.place.description, 'Test description')
        self.assertEqual(self.place.number_rooms, 2)
        self.assertEqual(self.place.number_bathrooms, 1)
        self.assertEqual(self.place.max_guest, 4)
        self.assertEqual(self.place.price_by_night, 100)
        self.assertEqual(self.place.latitude, 123.456)
        self.assertEqual(self.place.longitude, -78.901)
        self.assertEqual(self.place.amenity_ids, [1, 2, 3])

    def test_inheritance(self):
        """Test inheritance from BaseModel"""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_str_representation(self):
        """Test __str__ representation"""
        expected_str = "[Place] ({}) {}".format(self.place.id, self.place.__dict__)
        self.assertEqual(str(self.place), expected_str)

    def test_to_dict(self):
        """Test to_dict method"""
        place_dict = self.place.to_dict()
        self.assertIn('id', place_dict)
        self.assertIn('created_at', place_dict)
        self.assertIn('updated_at', place_dict)
        self.assertIn('__class__', place_dict)
        self.assertIn('city', place_dict)
        self.assertIn('user_id', place_dict)
        # Add assertions for other attributes

    def test_save_and_updated_at(self):
        """Test save method and updated_at attribute"""
        before_save = self.place.updated_at
        self.place.save()
        after_save = self.place.updated_at
        self.assertNotEqual(before_save, after_save)

    def test_load_from_dict(self):
        """Test loading Place instance from dictionary"""
        place_dict = self.place.to_dict()
        new_place = Place(**place_dict)
        self.assertEqual(self.place.id, new_place.id)
        self.assertEqual(self.place.created_at, new_place.created_at)
        self.assertEqual(self.place.updated_at, new_place.updated_at)
        self.assertEqual(self.place.city, new_place.city)
        self.assertEqual(self.place.user_id, new_place.user_id)
        # Add assertions for other attributes

if __name__ == '__main__':
    unittest.main()