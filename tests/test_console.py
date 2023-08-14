#!/usr/bin/python3
""" Unit test for console.py"""
import unittest
import io
import sys
from unittest.mock import patch
from console import HBNBCommand
import models.engine.file_storage

class TestHBNBCommand(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.console = HBNBCommand()

    def setUp(self):
        self.console_output = io.StringIO()
        self.saved_stdout = sys.stdout
        sys.stdout = self.console_output

    def tearDown(self):
        sys.stdout = self.saved_stdout

    def test_quit(self):
        """Test the 'quit' command"""
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")

    def test_create(self):
        """Test the 'create' command"""
        with patch("builtins.input", side_effect=["BaseModel"]):
            self.console.onecmd("create")
            self.assertIn("BaseModel.", self.console_output.getvalue())

    def test_show(self):
        """Test the 'show' command"""
        with patch("builtins.input", side_effect=["BaseModel", "123"]):
            self.console.onecmd("show")
            self.assertIn("** no instance found **", self.console_output.getvalue())

    def test_destroy(self):
        """Test the 'destroy' command"""
        with patch("builtins.input", side_effect=["BaseModel", "123"]):
            self.console.onecmd("destroy")
            self.assertIn("** no instance found **", self.console_output.getvalue())

    def test_all(self):
        """Test the 'all' command"""
        with patch("builtins.input", side_effect=["BaseModel"]):
            self.console.onecmd("all")
            self.assertIn("[]", self.console_output.getvalue())

    def test_update(self):
        """Test the 'update' command"""
        with patch("builtins.input", side_effect=["BaseModel", "123", "name", "MyModel"]):
            self.console.onecmd("update")
            self.assertIn("** no instance found **", self.console_output.getvalue())

    def test_count(self):
        """Test the 'count' command"""
        with patch("builtins.input", side_effect=["BaseModel"]):
            self.console.onecmd("count")
            self.assertIn("0", self.console_output.getvalue())

    def test_default(self):
        """Test default command behavior"""
        self.console.onecmd("invalid_command")
        self.assertIn("*** Unknown syntax:", self.console_output.getvalue())

if __name__ == '__main__':
    unittest.main()
