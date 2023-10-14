#!/usr/bin/python3
""" Review model extends BaseModel """
from .base_model import BaseModel


class Review(BaseModel):
    """ Review Model

    Attributes:
        place_id (str): ID of the place
        user_id (str): ID of the user
        text (str): Body of the review
    """
    place_id = ""
    user_id = ""
    text = ""
