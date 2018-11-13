#!/usr/bin/python
"""
test module
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models import storage


class TestUser(unittest.TestCase):
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

        self.a = User()
        self.a.email = "Heindrick@gmail.com"
        self.a.password = "Holberton"
        self.a.first_name = "Heiny"
        self.a.last_name = "Cheung"

        self.b = User()

    def test_email(self):
        """Setup Method

        Args:
            na
        Description:
            test string id of instance
        Return:
            na
        """

        self.assertNotEqual(self.a.email, "HC@gmail.com")
        self.assertTrue(self.a.email, "Heindrick@gmail.com")
        self.assertIsInstance(self.a.email, str)
        self.assertIsInstance(self.b.email, str)

    def test_password(self):
        """Setup Method

        Args:
            na
        Description:
            test string id of instance
        Return:
            na
        """

        self.assertEqual(type(self.b.password), str)
        self.assertIsNotNone(self.a.password)
        self.assertIsNotNone(self.b.password)
        self.assertEqual(self.a.password, "Holberton")

    def test_first_name(self):
        """Setup Method

        Args:
            na
        Description:
            test string id of instance
        Return:
            na
        """

        self.assertEqual(self.a.first_name, "Heiny")
        self.assertIsInstance(self.b.first_name, str)
        self.assertIsInstance(self.b.first_name, str)
        self.assertEqual(self.b.first_name, "")

    def test_last_name(self):
        """Setup Method

        Args:
            na
        Description:
            test string id of instance
        Return:
            na
        """

        self.assertEqual(self.a.last_name, "Cheung")
        self.assertIsInstance(self.a.last_name, str)
        self.assertIsInstance(self.b.last_name, str)
        self.assertEqual(self.b.last_name, "")

    def test_storage(self):
        """Setup Method

        Args:
            na
        Description:
            test string id of instance
        Return:
            na
        """
