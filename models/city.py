#!/usr/bin/python3
""" City Model inherits Base Model"""
from .base_model import BaseModel


class City(BaseModel):
    """ City Model

    Attributes:
        state_id (str): State.id
        name (str): City name
    """
    state_id = ""
    name = ""
