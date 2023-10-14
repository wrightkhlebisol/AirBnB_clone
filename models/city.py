#!/usr/bin/python3
""" City Model inherits Base Model"""
from .base_model import BaseModel


class City(BaseModel):
    """ City Model """

    state_id = ""
    name = ""
