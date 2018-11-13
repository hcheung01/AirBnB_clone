#!/usr/bin/python3
"""
class module
"""
from datetime import datetime
import uuid
import models


class BaseModel():
    """Base Class"""

    def __init__(self, *args, **kwargs):
        """Initialization Method

        Args:
            args: init args
            kwargs: keyword init args
        Description:
            initialize arguments
        Return:
            na
        """

        if kwargs:
            for key, val in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    dt_time_obj = datetime.strptime(val,
                                                    '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, dt_time_obj)
                elif key == '__class__':
                    pass
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """print object method

        Args:
            na
        Description:
            allows the user to print instance
        Return:
            na
        """

        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """update the public instance attribute

        Args:
            na
        Description:
            save instance
        Return:
            na
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns instance dictionary

        Args:
            na
        Description:
            create string of dictionary with instance information
        Return:
            na
        """

        dict2 = dict(self.__dict__)
        dict2['__class__'] = self.__class__.__name__
        dict2['created_at'] = self.created_at.isoformat()
        dict2['updated_at'] = self.updated_at.isoformat()
        return dict2
