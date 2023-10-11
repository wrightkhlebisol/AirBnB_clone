#!/usr/bin/python3
"""BaseModel that defines all common attributes/methods
"""
import uuid
from datetime import datetime


class BaseModel:
    """common attributes/methods for other classes
    """
    def __init__(self):
        """public instance method
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        updated_at = datetime.now()

    def __str__(self):
        """string method
        """
        class_name = f"[self.__class__.__name__]"
        obj_id = f"(self.id)"
        obj_dict = f"self.__dict__"
        return class_name + " " + obj_id + " " + obj_dict
        
