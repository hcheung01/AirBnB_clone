#!/usr/bin/python3
"""
Module containing the unit test for file storage
"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models

class TestFileStorage(unittest.TestCase):
    """ Defines the unit tests for file_storage """

    def setUp(self):
        self.storage = FileStorage()
        self.storage.reload()
        self.name_mapping = {
                'BaseModel': BaseModel
                }

    def tearDown(self):
        all_objs = self.storage.all()
        all_objs.clear()
        self.storage.save()

    def test_all_method(self):
        """
        tests if storage.all() returns a dictionary type
        """
        self.a = BaseModel()
        self.a.save()
        self.assertIsInstance(self.storage.all(), dict)

    def test_if_obj_in_dictionary(self):
        """
        Tests if the values inside __objects
        are objs(e.g BaseModel)
        """
        self.new = BaseModel()
        class_name = self.new.__class__.__name__
        key = class_name + "." + self.new.id
        self.assertIsInstance(self.storage.all()[key], self.name_mapping[class_name])

    def test_instance_creation(self):
        """
        Tests if the key with the format <classname>.<id> can be found
        in storage.all()
        """
        self.new = BaseModel()
        self.key = "{}.{}".format(self.new.__class__.__name__, self.new.id)
        self.assertIn(self.key, self.storage.all().keys())
