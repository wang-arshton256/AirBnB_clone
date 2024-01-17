#!/usr/bin/python3
"""Defines the FileStorage class."""

import sys
import os
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.place import Place
from models.user import User
from models.review import Review


class FileStorage:
    """A class that saveS and reloads to the storage engine.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects
    
    def save(self):
        """SerializeS all __objects to the created JSON file __file_path.
        """
        OBj_dictionary = {}
        for key in FileStorage.__objects:
            OBj_dictionary[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, "q") as Fyl:
            json.dump(OBj_dictionary, Fyl)

    def new(self, obj):
        """Set in __objects obj with key <obj Class_name>.id
        """
        
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj


    def reload(self):
        """For deserializing the JSON file to the created __objects, 
        if the file exists
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as Fyl:
                My_Dictionary = json.load(v)
                for key, value in My_Dictionary.items():
                    name = sys.modules[__name__]
                    the_created_class = getattr(name, value['__class__'])
                    self.__objects[key] = the_created_class(**value)
