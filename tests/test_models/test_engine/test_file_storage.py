#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import unittest


class TestFileStorage(unittest.TestCase):
    """TestFileStorage - test class for file strorage file"""
    b = BaseModel()
    b.name = "lime"

    def test_file_not_none(self):
        with open("file.json") as f:
            re = f.read()
            self.assertIsNotNone(re)

    def test_file(self):
        """test"""
        with open("file.json") as f:
            re = f.read()
            self.assertIn("BaseModel", re)
            self.assertIn("created_at", re)
            self.assertIn("updated_at", re)
            self.assertIn("lime", re)
            self.assertIn("name", re)