#!/usr/bin/python3
"""
class module
"""
import models
import uuid, datetime


class BaseModel():
    """Base Class"""

    def __init__(self):
        """Initialization Method"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """print object"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """update the public instance attribute"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns instance dictionary"""
        dict2 = dict(self.__dict__)
        dict2['__class__'] = self.__class__.__name__
        dict2['created_at'] = self.created_at.isoformat()
        dict2['updated_at'] = self.updated_at.isoformat()
        return dict2
