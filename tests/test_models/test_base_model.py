#!/usr/bin/python3
"""
Contains the unittests for BaseModel
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models import storage
import pep8
import os


class TestBaseModel(unittest.TestCase):
    """ Test Case for BaseModel """

    def setUp(self):
        """Setup Method

        Args:
            na
        Description:
            method will run before all test methods
        Return:
            na
        """

        self.a = BaseModel()
        self.b = BaseModel()
        self.old = BaseModel()
        self.old_dict = self.old.to_dict()
        self.new_model = BaseModel(**self.old_dict)

    def tearDown(self):
        """Tear down method"""

        del self.a
        del self.b
        del self.old
        del self.old_dict
        del self.new_model

        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8(self):
        """pep8 format"""

        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors.")

    def test_id_string(self):
        """Setup Method

        Args:
            na
        Description:
            test string id of instance
        Return:
            na
        """

        self.assertIsInstance(self.a.id, str)

    def test_created_at_type(self):
        """Create At Test Method

        Args:
            na
        Description:
            test datetime objects when creating instances
        Return:
            na
        """

        self.assertIsInstance(self.a.created_at, datetime)

    def test_updated_at_type(self):
        """Test Method

        Args:
            na
        Description:
            test datetime object whenever updating
        Return:
            na
        """

        self.assertIsInstance(self.a.updated_at, datetime)

    def test_dictionary_contents(self):
        """Test Method

        Args:
            na
        Description:
            test contents inside dictionary
        Return:
            na
        """

        self.assertTrue(getattr(self.a, '__class__'))
        self.assertTrue(getattr(self.a, 'created_at'))
        self.assertTrue(getattr(self.a, 'updated_at'))
        self.assertTrue(getattr(self.a, 'id'))
        with self.assertRaises(AttributeError):
            getattr(self.b, 'hemant')
        self.a.name = 'Heindrick'
        self.assertTrue(getattr(self.a, 'name'))

    def test_to_dict_return(self):
        ''' return value of the to_dict function is a dict

        Args:
            na
        Description:
            test whatever dictionary returns
        Return:
            na
        '''

        self.assertIsInstance(self.a.to_dict(), dict)

    def test_to_dict_good_types(self):
        ''' tests if values associated with certain keys are str types
            This is important for the created_at and updated_at keys

        Args:
            na
        Description:
            test existing keys in dictionary
        Return:
            na
        '''

        for key, values in self.a.to_dict().items():
            if key in ('id', 'created_at', '__class__', 'updated_at'):
                self.assertIsInstance(self.a.to_dict()[key], str)

    def test_newmodel_is_instance_of_base_model(self):
        """Test Method

        Args:
            na
        Description:
            test if new model is an instance of a class
        Return:
            na
        """

        self.assertIsInstance(self.new_model, BaseModel)

    def test_new_and_old_dicts_equal(self):
        """Setup Method

        Args:
            na
        Description:
            method will run before all test methods
        Return:
            na
        """

        self.assertDictEqual(self.old_dict, self.new_model.to_dict())

    def test_if_instances_are_unique(self):
        """Test Method

        Args:
            na
        Description:
            check if instance is unique
        Return:
            na
        """

        self.assertIsNot(self.old, self.new_model)

    def test_same_ids_different_instances(self):
        """
        If a new instance is created from the dictionary of a previous
        instance, the new instance's attributes should be the same.
        The previous test verifies if the two instances are unique.
        """
        self.assertEqual(self.old.id, self.new_model.id)
        self.assertEqual(
                self.old.created_at.__str__(),
                self.new_model.created_at.__str__())
        self.assertEqual(
                self.old.updated_at.__str__(),
                self.new_model.updated_at.__str__())

    def test_output_str(self):
        """ Tests if the output from print is a str

            Args:
                the instance

        """

        self.assertIsInstance(self.a.__str__(), str)

    def test_if_updated_at_changed(self):
        """
        Tests if the public instance attribute "updated_at"
        changed once the save method of the instance is called

        Args:
            the instance itself is passed
        """
        old_updated_at = self.a.updated_at.__str__()
        self.a.save()
        new_updated_at = self.a.updated_at.__str__()

        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_dunder_string(self):
        """ test method"""
        self.new = BaseModel()
        correct_output_str = "[{}] ({}) {}".format(
                self.new.__class__.__name__,
                self.new.id,
                self.new.__dict__)

        self.assertEqual(correct_output_str, self.new.__str__())

    def test_save(self):
        """test save method"""

        self.a.save()
        self.assertNotEqual(self.a.created_at, self.a.updated_at)

if __name__ == "__main__":
    unittest.main()
