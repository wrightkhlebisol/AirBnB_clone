#!/usr/bin/env python
""" FileStorage class serializes instances to a JSON 
file and deserializes JSON file to instances """
import json


class FileStorage():
    
    __file_path = None
    __objects = {}

    def all(self):
        """
            Get all object members

            Returns: __objects (dict)
        """
        return __objects

    def new(self, obj):
        """
            Sets private class attribute __object to given 
            object (obj) with key "classname.obj[id]"
        """
        key = f"{}.{}".format(self.__class__.__name__, obj.get("id"))
        __objects[key] = obj

    def save(self):
        """
            Serializes the object to JSON and save to file
        """
        with open(__file_path, "w", encoding="utf-8") as f:
            json.dump(__objects, f)

    def reload(self):
        
        pass
