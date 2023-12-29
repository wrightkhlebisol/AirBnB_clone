#!/usr/bin/python3
"""Defines common attributes/methods for other classes."""
import uuid
from datetime import datetime
from models import storage 


class BaseModel:
    """Base Model for all classes."""

    def __init__(self, *args, **kwargs):
        """Initialize instances."""
        if (kwargs):
            for key in kwargs.keys():
                if key == '__class__':
                    continue

                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.fromisoformat(kwargs[key])
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """Update updated_at with current datetime."""
        self.updated_at = datetime.now().isoformat()
        storage.save()

    def to_dict(self):
        """Return dict with key/values of __dict__ of the instance."""
        inst_dict = {}
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        inst_dict.update(self.__dict__)
        inst_dict['__class__'] = self.__class__.__name__

        return (inst_dict)

    def __str__(self):
        """Print class structure."""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")
