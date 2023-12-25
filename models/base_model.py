#!/usr/bin/python3
"""Defines common attributes/methods for other classes."""
import uuid
from datetime import datetime


class BaseModel:
    """Base Model for all classes."""

    def __init__(self):
        """Initialize instances."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Update updated_at with current datetime."""
        self.updated_at = datetime.now()

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
