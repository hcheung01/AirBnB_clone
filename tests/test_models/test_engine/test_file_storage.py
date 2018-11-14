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
        """
        setUp function that runs before every test
        """
        self.storage = FileStorage()
        self.storage.reload()
        self.name_mapping = {
            'BaseModel': BaseModel
        }

    def tearDown(self):
        """
        runs after every test method
        """
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
        self.assertIsInstance(
            self.storage.all()[key], self.name_mapping[class_name])

    def test_instance_creation(self):
        """
        Tests if the key with the format <classname>.<id> can be found
        in storage.all()
        """
        self.new = BaseModel()
        self.key = "{}.{}".format(self.new.__class__.__name__, self.new.id)
        self.assertIn(self.key, self.storage.all().keys())

    def test_storage_file_path_str(self):
        """
        Checks if the private class attribute is a str
        """

        self.assertIsInstance(self.storage._FileStorage__file_path, str)

    def test_save_method(self):
        """
        Tests if the save functionality of the class works
        """
        import json
        self.new = BaseModel()
        self.new.save()
        with open('file.json', 'r') as file:
            json_string = file.read()
        key = "{}.{}".format('BaseModel', self.new.id)
        ref_dict = {key: self.new.to_dict()}
        dict_after_load = json.loads(json_string)
        self.assertEqual(ref_dict, dict_after_load)

    def test_reload_json_file_no_existo(self):
        """
        Tests if reload raises a FileNotFoundError when
        the json file is removed
        """
        import os

        os.remove("file.json")
        self.assertRaises(FileNotFoundError, self.storage.reload())

    def test_reload_json_empty(self):
        """
        Tests if reload loads an empty dictionary
        """

        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 0)

    def test_reload_json_has_something(self):
        """
        Tests if the json file is not empty and reload
        loads a key and a dictionary into __objects
        """
        self.new = BaseModel()
        self.new.save()
        self.key = "{}.{}".format('BaseModel', self.new.id)

        self.storage.reload()
        self.all_objs = self.storage.all()

        self.assertIsInstance(self.all_objs[self.key], BaseModel)

    def test_new_method(self):
        """
        Tests if the new method is adding instances to the storage dictionary
        """

        self.a = BaseModel()
        self.key = 'BaseModel.{}'.format(self.a.id)
        self.assertIn(self.key, self.storage.all())
