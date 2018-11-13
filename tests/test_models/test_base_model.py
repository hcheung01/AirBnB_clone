#!/usr/bin/python3
""" Contains the unittests for BaseModel """
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """ Test Case for BaseModel """

    def setUp(self):
        self.a = BaseModel()
        self.b = BaseModel()
        self.old = BaseModel()
        self.old_dict = self.old.to_dict()
        self.new_model = BaseModel(**self.old_dict)

    def test_id_string(self):
        self.assertIsInstance(self.a.id, str)

    def test_created_at_type(self):
        self.assertIsInstance(self.a.created_at, datetime)

    def test_updated_at_type(self):
        self.assertIsInstance(self.a.updated_at, datetime)

    def test_dictionary_contents(self):
        self.assertTrue(getattr(self.a, '__class__'))
        self.assertTrue(getattr(self.a, 'created_at'))
        self.assertTrue(getattr(self.a, 'updated_at'))
        self.assertTrue(getattr(self.a, 'id'))
        with self.assertRaises(AttributeError):
            getattr(self.b, 'hemant')
        self.a.name = 'Heindrick'
        self.assertTrue(getattr(self.a, 'name'))

    def test_to_dict_return(self):
        ''' return value of the to_dict function is a dict '''
        self.assertIsInstance(self.a.to_dict(), dict)

    def test_to_dict_good_types(self):
        ''' tests if values associated with certain keys are str types
            This is important for the created_at and updated_at keys
        '''
        for key, values in self.a.to_dict().items():
            if key in ('id', 'created_at', '__class__', 'updated_at'):
                self.assertIsInstance(self.a.to_dict()[key], str)

    def test_newmodel_is_instance_of_base_model(self):
        self.assertIsInstance(self.new_model, BaseModel)

    def test_new_and_old_dicts_equal(self):
        self.assertDictEqual(self.old_dict, self.new_model.to_dict())

    def test_if_instances_are_unique(self):
        self.assertIsNot(self.old, self.new_model)

    @unittest.skip('wip')
    def test_instance_creation_add_to_storage_dict(self):
        self.test = BaseModel()
        self.test.save()
        key = '{}.{}'.format(type(self.test).__name__, self.test.id)
        self.assertTrue(getattr(storage.all(), key))


