from datetime import datetime
from models.amenity import Amenity
import unittest
"""
Test Amenity Module
"""

class TestAmenity(unittest.TestCase):
    """
    The test Amenity class
    """
    
    @classmethod
    def setUpClass(cls):
        """
        Setting up the class
        """
        cls.bm = Amenity()
        cls.n = datetime.now()
        cls.bm2 = Amenity()
        cls.n2 = datetime.now()

        cls.assert_equal = cls.assertEqual
        cls.assert_not_equal = cls.assertNotEqual
        cls.assert_in = cls.assertIn
        cls.assert_not_in = cls.assertNotIn
        cls.assert_almost_equal = cls.assertAlmostEqual  
        cls.assert_not_almost_equal = cls.assertNotAlmostEqual  
        cls.assert_instance = cls.assertIsInstance
        cls.assert_not_instance = cls.assertNotIsInstance
        
if __name__ == '__main__':
    unittest.main()