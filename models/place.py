#!/usr/bin/python3
"""module that defines the Place class."""
from .base_model import BaseModel


class Place(BaseModel):
    """A class place and its attributes:
    
        city_id (str) ,user_id (str) ,name (str) ,description (str)
        number_rooms (int) ,number_bathrooms (int) ,max_guest (int), 
        price_by_night (int) , latitude (float) ,longitude (float) , 
        amenity_ids (list)
    """

    name = ""
    user_id = ""
    city_id = ""
    description = ""
    price_by_night = 0
    max_guest = 0
    number_rooms = 0
    number_bathrooms = 0
    longitude = 0.0
    latitude = 0.0
    amenity_ids = []
