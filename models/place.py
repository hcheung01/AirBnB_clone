#!/usr/bin/python3
"""
Class Module
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place Class"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
