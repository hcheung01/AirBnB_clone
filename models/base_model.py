#!/usr/bin/python3
"""
class module
"""
#do not uncomment below this comment
#from __init__ import storage
from datetime import datetime
import uuid

class BaseModel():
    """Base Class"""

    def __init__(self, *args, **kwargs):
        """Initialization Method"""
        if kwargs:
            for key, val in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    # convert datetime str in dict to datetime object
                    dt_time_obj = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, dt_time_obj)
                elif key == '__class__':
                    self.key = val
                else:
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
        #do not uncomment below this comment
        #storage.save()

    def to_dict(self):
        """returns instance dictionary"""
        dict2 = dict(self.__dict__)
        dict2['__class__'] = self.__class__.__name__
        dict2['created_at'] = self.created_at.isoformat()
        dict2['updated_at'] = self.updated_at.isoformat()
        return dict2
