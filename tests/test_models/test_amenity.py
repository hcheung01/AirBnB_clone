#!/usr/bin/python3
"""
Test Module
"""
from models.base_model import BaseModel
from models.amenity import Amenity
import unittest
import pep8
import os


class TestAmenity(unittest.TestCase):
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

        self.a = Amenity()
        self.a.name = "Hemant"
        self.b = Amenity()

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
            check if obj is instance of Amenity class
        Return:
            na
        """

        self.assertIsInstance(self.a, Amenity)
        self.assertIsInstance(self.b, Amenity)

    def test_has_attr(self):
        """test method

        Description:
            check if attr in instance
        Return:
            na
        """

        self.assertTrue('name' in self.a.__dict__)
        self.assertFalse('newname' in self.b.__dict__)

    def test_name_attr(self):
        """test method to

        Args:
            na
        Description:
            check attr exist and value
        Return:
            na
        """

        self.assertEqual(self.a.name, "Hemant")
        self.assertEqual(self.b.name, "")
        self.assertFalse(self.b.name)

    def test_set_attr(self):
        """test method to

        Args:
            na
        Description:
            set existing attr
        Return:
            na
        """

        self.a.name = "New value"
        self.b.name = "Now there is a value"

        self.assertEqual(self.a.name, "New value")
        self.assertEqual(self.b.name, "Now there is a value")

    def test_attr_type(self):
        """test method to

        Args:
            na
        Description:
            check type of attribute value
        Return:
            na
        """

        self.assertIsInstance(self.a.name, str)

    def test_inherit(self):
        """test method

        Args:
            na
        Description:
            if subclass of BaseModel
        Return:
            na
        """

        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_save(self):
        """test save method"""

        self.b.save()
        self.assertNotEqual(self.b.created_at, self.b.updated_at)

if __name__ == "__main__":
    unittest.main()
