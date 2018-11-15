"""
Test Module
"""
from models.review import Review
from models.base_model import BaseModel
import unittest
import pep8
import os


class TestReview(unittest.TestCase):
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

        self.a = Review()
        self.a.place_id = "1000"
        self.a.user_id = "1000"
        self.a.text = "1000"
        self.b = Review()

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

        self.assertIsInstance(self.a, Review)
        self.assertIsInstance(self.b, Review)

    def test_attr_exists(self):
        """test method
        Args:
            na
        Description:
            check if attribute exist
        Return:
            na
        """

        self.assertTrue('place_id' in self.a.__dict__)
        self.assertTrue('user_id' in self.a.__dict__)
        self.assertTrue('text' in self.a.__dict__)
        self.assertFalse('place_id' in self.b.__dict__)
        self.assertFalse('user_id' in self.b.__dict__)
        self.assertFalse('text' in self.b.__dict__)
        self.assertTrue(self.a.place_id)
        self.assertTrue(self.a.user_id)
        self.assertTrue(self.a.text)
        self.assertFalse(self.b.place_id)
        self.assertFalse(self.b.user_id)
        self.assertFalse(self.b.text)

    def test_attr_value(self):
        """test method

        Args:
            na
        Description:
            check attribute value
        Return:
            na
        """

        self.assertNotEqual(self.a.place_id, "10000")
        self.assertEqual(self.a.place_id, "1000")
        self.assertEqual(self.a.user_id, "1000")
        self.assertEqual(self.a.text, "1000")

        self.assertEqual(self.b.place_id, "")
        self.assertEqual(self.b.user_id, "")
        self.assertEqual(self.b.text, "")

    def test_attr_type(self):
        """test method

        Args:
            na
        Description:
            check attribute type
        Return:
            na
        """

        self.assertEqual(type(self.a.place_id), str)
        self.assertEqual(type(self.a.user_id), str)
        self.assertEqual(type(self.a.text), str)
        self.assertEqual(type(self.b.place_id), str)
        self.assertEqual(type(self.b.user_id), str)
        self.assertEqual(type(self.b.text), str)

    def test_inherit(self):
        """test method

        Args:
            na
        Description:
            if subclass of BaseModel
        Return:
            na
        """

        self.assertTrue(issubclass(Review, BaseModel))

    def test_save(self):
        """test save"""

        self.b.save()
        self.assertNotEqual(self.b.created_at, self.b.updated_at)

if __name__ == "__main__":
    unittest.main()
