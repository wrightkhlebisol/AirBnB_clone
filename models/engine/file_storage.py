#!/usr/bin/python3
""" FileStorage class serializes instances to a JSON
file and deserializes JSON file to instances """
import json
import os


class FileStorage():
    """File Storage class that serializes and deserializes
    """

    __file_path = 'file.json'
    __objects = {}

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
        key = f"{self.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj.to_dict()

    def save(self):
        """
            Serializes object to JSON and save to file
        """
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """
            Deserializes JSON file to __objects
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, encoding="utf-8") as f:
                self.__objects = json.load(f)
