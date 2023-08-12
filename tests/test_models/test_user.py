#!/usr/bin/python3
from datetime import datetime
from models.user import User
import unittest
"""Test User module"""


class TestUser(unittest.TestCase):
    """Test User class"""

    @classmethod
    def setUpClass(cls):
        """Set up class"""
        cls.bm = User()
        cls.n = datetime.now()
        cls.bm2 = User()
        cls.n2 = datetime.now()
        cls.ae = cls.assertEqual
        cls.ane = cls.assertNotEqual
        cls.ai = cls.assertIn
        cls.ani = cls.assertNotIn
        cls.aii = cls.assertIsInstance
        cls.anii = cls.assertNotIsInstance