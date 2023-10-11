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
        class_name = self.__class__.__name__
        obj_id = self.id
        obj_dict = self.__dict__
        return f"[{class_name}] ({obj_id}) {obj_dict}" 
