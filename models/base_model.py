#!/usr/bin/python3
"""This module contains the BaseModel class"""
from datetime import datetime
import uuid


class BaseModel():
    """The base class for all the other classes to
        inherit from"""

    def __init__(self, *args, **kwargs):
        """Initializes a new instance"""
        if not 'id' in kwargs:
            self.id = str(uuid.uuid4())
        if not 'created_at' in kwargs:
            self.created_at = datetime.now()
        if not 'updated_at' in kwargs:
            self.updated_at = datetime.now()

        for key, value in kwargs.items():
            if key != '__class__':
                setattr(self, key, value)
            if key == 'created_at' or key == 'updated_at':
                value = datetime.fromisoformat(value)
                setattr(self, key, value)

    def __str__(self):
        """
        Converts this object to a readable string
        Return
            str: The string representation of this object
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def to_dict(self):
        """
        Returns a dictionary containing all keys/ values of __dict__.
        Includes an extra '__class__' key value pair and converts
        datetime object to strings.
        Returns:
            (dict): The dictionary representation of the object
        """
        dictionary = dict(self.__dict__)
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary['__class__'] = self.__class__.__name__

        return dictionary

    def save(self):
        """
        Updates the updated_at attribute of this object
        """
        self.updated_at = datetime.now()
