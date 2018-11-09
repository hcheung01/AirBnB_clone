#!/usr/bin/python3
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
