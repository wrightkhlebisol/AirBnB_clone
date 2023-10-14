#!/usr/bin/python3
""" Amenity class inherits Base Model """
from .base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity Class

    Attributes:
        name (str): Name of the amenity
    """
    name = ""
