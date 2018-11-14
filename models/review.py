#!/usr/bin/python3
"""
Class Module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class which inherits from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
