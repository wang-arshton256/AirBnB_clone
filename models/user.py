#!/usr/bin/python3
"""module that defines the User class."""
from .base_model import BaseModel


class User(BaseModel):
    """Represent a User
    Attr:
        Fname (str): First name
        Lname (str): Last name
        email (str): Email
        pass (str): User password
    """

    first_name = ""
    last_name = ""
    email = ""
    password = ""
