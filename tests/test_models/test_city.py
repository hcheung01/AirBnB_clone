#!/usr/bin/python3
"""
Test Module
"""
from models.city import City
from models.base_model import BaseModel
from models import storage
import unittest


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
        self.a.state_id = "1000Holberton"
        self.a.name = "Hemant"

        self.b = City()

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
        self.assertEqual(self.a.state_id, "1000Holberton")
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
