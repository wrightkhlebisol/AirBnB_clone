#!/usr/bin/python3
""" Review model extends BaseModel """
from .base_model import BaseModel


class Review(BaseModel):
    """ Review Model """

    place_id = ""
    user_id = ""
    text = ""
