#!/usr/bin/python3
""" Place model inherits Base Model"""
from .base_model import BaseModel


class Place(BaseModel):
    """Place Model

    Attributes:
        city_id (str): City.id
        user_id (str): User.id
        name (str): Name of the place
        description (str): Details 
        number_rooms (int): No of rooms
        number_bathrooms (int): No of Baths
        max_guest (int): Max allowed guest
        price_by_night (int): Price per night
        latitude (float): Latitude of the place
        longitude (float): Longitude of the place
        amenity_ids (list): List of amenity.id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
