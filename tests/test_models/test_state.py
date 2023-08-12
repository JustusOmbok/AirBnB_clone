#!/usr/bin/python3
from datetime import datetime
from models.state import State
import unittest
"""Test State module"""


class TestState(unittest.TestCase):
    """Test State class"""

    @classmethod
    def setUpClass(cls):
        """Set up class"""
        cls.bm = State()
        cls.n = datetime.now()
        cls.bm2 = State()
        cls.n2 = datetime.now()
        cls.ae = cls.assertEqual
        cls.ane = cls.assertNotEqual
        cls.ai = cls.assertIn
        cls.ani = cls.assertNotIn
        cls.aii = cls.assertIsInstance
        cls.anii = cls.assertNotIsInstance