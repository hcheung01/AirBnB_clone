#!/usr/bin/python3
"""
Class Module
"""
from models.base_model import BaseModel
from models.state import State

class City(BaseModel):
    """Class City which inherits from Base class"""

    state_id = ''
    name = ''
