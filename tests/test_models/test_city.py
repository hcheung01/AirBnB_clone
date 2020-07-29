#!/usr/bin/python3
"""
Test Module
"""
from models.city import City
from models.base_model import BaseModel
from models import storage
import unittest
import os
import pep8


class TestCity(unittest.TestCase):
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

        self.a = City()
        self.a.state_id = "1000Coding"
        self.a.name = "Hemant"
        self.b = City()

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

        self.assertIsInstance(self.a, City)
        self.assertIsInstance(self.b, City)

    def test_attr_exists(self):
        """test method
        Args:
            na
        Description:
            check if attribute exist
        Return:
            na
        """

        self.assertTrue('state_id' in self.a.__dict__)
        self.assertTrue('name' in self.a.__dict__)
        self.assertFalse('state_id' in self.b.__dict__)
        self.assertFalse('name' in self.b.__dict__)

        self.assertTrue(self.a.state_id)
        self.assertTrue(self.a.name)
        self.assertFalse(self.b.state_id)
        self.assertFalse(self.b.name)

    def test_state_id(self):
        """test method

        Args:
            na
        Description:
            check state_id attribute
        Return:
            na
        """

        self.assertNotEqual(self.a.state_id, "Heindrick")
        self.assertEqual(self.a.state_id, "1000Coding")
        self.assertEqual(self.b.state_id, "")
        self.assertEqual(type(self.a.state_id), str)
        self.assertEqual(type(self.b.state_id), str)

    def test_name(self):
        """test method

        Args:
            na
        Description:
            check name attribute
        Return:
            na
        """

        self.assertEqual(self.a.name, "Hemant")
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

        self.assertTrue(issubclass(City, BaseModel))

    def test_save(self):
        """test save"""

        self.b.save()
        self.assertNotEqual(self.b.created_at, self.b.updated_at)

if __name__ == "__main__":
    unittest.main()
