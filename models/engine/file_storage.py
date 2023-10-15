#!/usr/bin/python3
""" FileStorage class serializes instances to a JSON
file and deserializes JSON file to instances """
import json
import os

from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage():
    """File Storage class that serializes and deserializes
    """

    __file_path = 'file.json'
    __objects = {}
    class_dict = {
        'Amenity': 'amenity',
        'BaseModel': 'base_model',
        'City': 'city',
        'Place': 'place',
        'Review': 'review',
        'State': 'state',
        'User': 'user'
    }

    def all(self):
        """
            Get all object members

            Returns: __objects (dict)
        """
        return self.__objects

    def new(self, obj):
        """
            Sets private class attribute __object to given
            object (obj) with key "classname.obj[id]"
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
            Serializes object to JSON and save to file
        """
        with open(self.__file_path, "w", encoding="utf-8") as f:
            _obj = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(_obj, f)

    def reload(self):
        """
            Deserializes JSON file to __objects
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                json_dict = json.load(f)
                for obj in json_dict.values():
                    class_n = obj['__class__']
                    module_n = self.class_dict[class_n]
                    del obj['__class__']
                    self.new(eval(f'{module_n}.{class_n}')(**obj))
