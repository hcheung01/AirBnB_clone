#!/usr/bin/python3
"""
class module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class which inherits from BaseModel"""

    email = ''
    password = ''
    first_name = ''
    last_name = ''
