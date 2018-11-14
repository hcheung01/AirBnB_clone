#!/usr/bin/python3
"""
Class Module
"""
from models.base_model import BaseModel
from models.place import Place
from models.user import User

class Review(BaseModel):
    """Review Class which inherits from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
