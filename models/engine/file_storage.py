#!/usr/bin/python3
"""
class module
"""
from models.base_model import BaseModel
import json
import models

class FileStorage():
    """class for serialization"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets objs in objs dictionary"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serializes objects in dictionary"""
        dicts = {}
        for obj_id, obj in self.__objects.items():
            #call to_dic method in each object to return str dict
            dicts[obj_id] = obj.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(dicts, f)

    def reload(self):
        """deserializes the JSON file in dictionary"""
