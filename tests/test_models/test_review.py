#!/usr/bin/python3
from datetime import datetime
from models.review import Review
import unittest
"""Test Review module"""


class TestReview(unittest.TestCase):
    """Test Review class"""

    @classmethod
    def setUpClass(cls):
        """Set up class"""
        cls.bm = Review()
        cls.n = datetime.now()
        cls.bm2 = Review()
        cls.n2 = datetime.now()
        cls.ae = cls.assertEqual
        cls.ane = cls.assertNotEqual
        cls.ai = cls.assertIn
        cls.ani = cls.assertNotIn
        cls.aii = cls.assertIsInstance
        cls.anii = cls.assertNotIsInstance