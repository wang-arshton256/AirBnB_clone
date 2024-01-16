#!/usr/bin/python3
"""Class Module for FileStorage"""
from models.base_model import BaseModel
import os
import json


class FileStorage():
    """
    A file storage class that saves and relodes to a JSON file and
    """
    
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """To return the __objects dictionary"""
        return FileStorage.__objects