#!/usr/bin/python3
"""User Model that inherits from BaseModel """
from .base_model import BaseModel


class User(BaseModel):
    """ User Model

    Attributes:
        email (str): USer email
        password (str): User password
        first_name (str): First name
        last_name (str): Last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
