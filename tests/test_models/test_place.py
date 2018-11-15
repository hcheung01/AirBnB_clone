#!/usr/bin/python3
"""
Test Module
"""
from models.base_model import BaseModel
from models.place import Place
import unittest
import pep8
import os


class TestPlace(unittest.TestCase):
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

        self.a = Place()
        self.a.city_id = "1a2b3c"
        self.a.user_id = "Hcheung01"
        self.a.name = "Heindrick"
        self.a.description = "Test objects"
        self.a.number_rooms = 4
        self.a.number_bathrooms = 3
        self.a.max_guest = 10
        self.a.price_by_night = 100
        self.a.latitude = 11.5
        self.a.longitude = 8.5
        self.a.amenity_ids = ["one", "two", "three"]
        self.b = Place()

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

        self.assertIsInstance(self.a, Place)
        self.assertIsInstance(self.b, Place)

    def test_has_attr(self):
        """test method

        Description:
            check if attr in instance
        Return:
            na
        """

        self.assertTrue('city_id' in self.a.__dict__)
        self.assertTrue('user_id' in self.a.__dict__)
        self.assertTrue('name' in self.a.__dict__)
        self.assertTrue('description' in self.a.__dict__)
        self.assertTrue('number_rooms' in self.a.__dict__)
        self.assertTrue('number_bathrooms' in self.a.__dict__)
        self.assertTrue('max_guest' in self.a.__dict__)
        self.assertTrue('price_by_night' in self.a.__dict__)
        self.assertTrue('latitude' in self.a.__dict__)
        self.assertTrue('longitude' in self.a.__dict__)
        self.assertTrue('amenity_ids' in self.a.__dict__)
        self.assertFalse('city_id' in self.b.__dict__)
        self.assertFalse('user_id' in self.b.__dict__)
        self.assertFalse('name' in self.b.__dict__)
        self.assertFalse('description' in self.b.__dict__)
        self.assertFalse('number_rooms' in self.b.__dict__)
        self.assertFalse('number_bathrooms' in self.b.__dict__)
        self.assertFalse('max_guest' in self.b.__dict__)
        self.assertFalse('price_by_night' in self.b.__dict__)
        self.assertFalse('latitude' in self.b.__dict__)
        self.assertFalse('longitude' in self.b.__dict__)
        self.assertFalse('amenity_ids' in self.b.__dict__)

    def test_attr_value(self):
        """test method to

        Args:
            na
        Description:
            check attr exist and value
        Return:
            na
        """

        self.assertEqual(self.a.city_id, "1a2b3c")
        self.assertEqual(self.a.user_id, "Hcheung01")
        self.assertEqual(self.a.name, "Heindrick")
        self.assertEqual(self.a.description, "Test objects")
        self.assertEqual(self.a.number_rooms, 4)
        self.assertEqual(self.a.number_bathrooms, 3)
        self.assertEqual(self.a.max_guest, 10)
        self.assertEqual(self.a.price_by_night, 100)
        self.assertEqual(self.a.latitude, 11.5)
        self.assertEqual(self.a.longitude, 8.5)
        self.assertEqual(self.a.amenity_ids, ["one", "two", "three"])

    def test_set_attr(self):
        """test method to

        Args:
            na
        Description:
            set existing attr to new value
        Return:
            na
        """

        self.a.city_id = "new"
        self.a.user_id = "new"
        self.a.name = "new"
        self.a.description = "new"
        self.a.number_rooms = 111
        self.a.number_bathrooms = 111
        self.a.max_guest = 111
        self.a.price_by_night = 111
        self.a.latitude = 11.1
        self.a.longitude = 11.1
        self.a.amenity_ids = ["one", "one", "one"]
        self.assertEqual(self.a.city_id, "new")
        self.assertEqual(self.a.user_id, "new")
        self.assertEqual(self.a.name, "new")
        self.assertEqual(self.a.description, "new")
        self.assertEqual(self.a.number_rooms, 111)
        self.assertEqual(self.a.number_bathrooms, 111)
        self.assertEqual(self.a.max_guest, 111)
        self.assertEqual(self.a.price_by_night, 111)
        self.assertEqual(self.a.latitude, 11.1)
        self.assertEqual(self.a.longitude, 11.1)
        self.assertEqual(self.a.amenity_ids, ["one", "one", "one"])

    def test_attr_type(self):
        """test method to

        Args:
            na
        Description:
            check type of attribute value
        Return:
            na
        """

        self.assertIsInstance(self.a.city_id, str)
        self.assertIsInstance(self.a.user_id, str)
        self.assertIsInstance(self.a.name, str)
        self.assertIsInstance(self.a.description, str)
        self.assertIsInstance(self.a.number_rooms, int)
        self.assertIsInstance(self.a.number_bathrooms, int)
        self.assertIsInstance(self.a.max_guest, int)
        self.assertIsInstance(self.a.price_by_night, int)
        self.assertIsInstance(self.a.latitude, float)
        self.assertIsInstance(self.a.longitude, float)
        self.assertIsInstance(self.a.amenity_ids, list)

    def test_list_of_strings(self):
        """test method to

        Args:
            na
        Description:
            check if amenity_ids is a list of string elements
        Return:
            na
        """

        for elem in self.a.amenity_ids:
            self.assertEqual(type(elem), str)

    def test_inherit(self):
        """test method

        Args:
            na
        Description:
            if subclass of BaseModel
        Return:
            na
        """

        self.assertTrue(issubclass(Place, BaseModel))

    def test_save(self):
        """test save"""

        self.b.save()
        self.assertNotEqual(self.b.created_at, self.b.updated_at)

if __name__ == "__main__":
    unittest.main()
