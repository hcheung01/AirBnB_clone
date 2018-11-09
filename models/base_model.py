#!/usr/bin/python3
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
