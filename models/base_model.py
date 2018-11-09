#!/usr/bin/python3
<<<<<<< HEAD
"""
class module
"""
from datetime import datetime
import uuid

class BaseModel():
    """Base Class"""

    def __init__(self, *args, **kwargs):
        """Initialization Method"""
        if kwargs:
            for key, val in kwargs.items():
                if key == 'create_at' or key == 'updated_at':
                    dt_time_obj = datetime.strftime(val, '%Y, %-m, %-d', )
                setattr(self, key, val)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    # print the class
    def __str__(self):
        """print object"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    # update datetime
    def save(self):
        """update the public instance attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns instance dictionary"""
        dict2 = dict(self.__dict__)
        dict2['__class__'] = self.__class__.__name__
        dict2['created_at'] = self.created_at.isoformat()
        dict2['updated_at'] = self.updated_at.isoformat()
        return dict2
=======
""" Contains the base model class """


import uuid
import datetime


class BaseModel:
    """ Contains common attributes and methods child classes will use """

    def __init__(self):
        """ method called when an instance of the class is created
        """

        self.id = str(uuid.uuid4())

    def __str__(self):
        """ prints a  user representation of an instane of the class """
        return("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))


if __name__ == '__main__':
    a = BaseModel()
    print(a)
>>>>>>> 570e7508c8b03fa8d6b408121cce6bcaf6ec923a
