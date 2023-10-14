#!/usr/bin/python3
""" State Model inherits Base Model """
from .base_model import BaseModel


class State(BaseModel):
    """ State Model

    Attributes:
        name (str): State name
    """
    name = ""
