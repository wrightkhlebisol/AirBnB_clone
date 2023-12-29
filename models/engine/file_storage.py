#!/usr/bin/python3
"""Serializes instances to JSON and deserializes to instances."""
import json
import os


class FileStorage:
    """Class that handles serializing and deserializing."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return all objects."""
        return self.__objects

    def new(self, obj):
        """Set the given obj in __object, essentially appending."""
        obj_name = obj.__class__.__name__
        obj_id = obj.id
        obj.created_at = obj.created_at.isoformat()
        obj.updated_at = obj.updated_at.isoformat()
        obj_dict = obj.__dict__
        self.__objects[f'{obj_name}.{obj_id}'] = obj_dict

    def save(self):
        """Serialize objects to the JSON file."""
        with open(self.__file_path, 'w', encoding="utf-8") as fh:
            json.dump(self.__objects, fh)

    def reload(self):
        """
        Deserialize the JSON file if it exists.

        It will check for the existence of the file,
        if it exists, it writes to it, else, do nothing
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as fh:
                self.__objects = json.load(fh)
