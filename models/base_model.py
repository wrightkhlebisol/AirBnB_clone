#!/usr/bin/python3
"""BaseModel that defines all common attributes/methods
"""
import storage
import uuid
from datetime import datetime


class BaseModel:
    """common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """public instance attributes
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """string method

            Retuns: classname (str)
                    id (str)
                    dictionary (str)
        """
        class_name = self.__class__.__name__
        obj_id = self.id
        obj_dict = self.__dict__
        return f"[{class_name}] ({obj_id}) {obj_dict}"

    def save(self):
        """updates public instance variable updated_at
        """
        self.updated_at = datetime.now()
        storage.save(self)

    def to_dict(self):
        """returns dictionary containing all keys/values
        of __dict__ of the instance

        Returns: __dict__ (dictionary)
        """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
