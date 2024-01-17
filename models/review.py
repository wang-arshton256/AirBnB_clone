#!/usr/bin/python3
"""module that defines the Review class."""
from .base_model import BaseModel


class Review(BaseModel):
    """ A review class

    Attr:
        user_id (str):
        place_id (str):
        text (str):
    """

    user_id = ""
    place_id = ""
    text = ""
