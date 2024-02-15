#!/usr/bin/python3
"""This is the file storage class"""
import json
import os


class FileStorage:
    """This is the class for the file storage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the __objects dictionary"""
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the dictionary
        Args:
            obj: The object to be added
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self):
        """
        serializes all the objects to the file
        """
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """
        Deserializes all the objects from the storage file
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                self.__objects = json.load(f)
