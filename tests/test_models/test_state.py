#!/usr/bin/python3
"""
Test Module
"""
from models.state import State
from models.base_model import BaseModel
from models import storage
import unittest
import pep8
import os


class TestState(unittest.TestCase):
    """test User Class"""

    def setUp(self):
        """Setup Method

        Args:
            na
        Description:
            method will run before all test methods
        Return:
            na
        """

        self.a = State()
        self.a.name = "Heindrick"
        self.b = State()

    def tearDown(self):
        """teardown method

        Args:
            na
        Description:
            remove testing instances and delete file.json file
        Return:
            na
        """

        del self.a
        del self.b
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8_conformance(self):
        """Test that we conform to PEP8"""

        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors.")

    def test_instance(self):
        """test method
        Args:
            na
        Description:
            check if instance is of class State
        Return:
            na
        """

        self.assertIsInstance(self.a, State)
        self.assertIsInstance(self.b, State)

    def test_attr_exists(self):
        """test method
        Args:
            na
        Description:
            check if attribute exist
        Return:
            na
        """

        self.assertTrue('name' in self.a.__dict__)
        self.assertFalse('newname' in self.b.__dict__)

    def test_name(self):
        """test method

        Args:
            na
        Description:
            check name attribute
        Return:
            na
        """

        self.assertEqual(self.a.name, "Heindrick")
        self.assertEqual(self.b.name, "")
        self.assertEqual(type(self.a.name), str)
        self.assertEqual(type(self.b.name), str)

    def test_inherit(self):
        """test method

        Args:
            na
        Description:
            if subclass of BaseModel
        Return:
            na
        """

        self.assertTrue(issubclass(State, BaseModel))

    def test_save(self):
        """test save"""

        self.b.save()
        self.assertNotEqual(self.b.created_at, self.b.updated_at)

if __name__ == "__main__":
    unittest.main()
