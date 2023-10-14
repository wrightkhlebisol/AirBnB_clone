#!/usr/bin/python3
"""User Model that inherits from BaseModel """
from .base_model import BaseModel


class User(BaseModel):
    """ User Model """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
