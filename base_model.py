#!/usr/bin/python3
"""Model for Basemodel class"""
import uuid
from datetime import datetime
from . import storage


class Basemodel:
    """The Basemodel class defines all common attributes for other classes"""
    
    def __init__(self, *args, **kwargs):
        """initializes and instance"""
        if len(kwargs) >= 0:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    val = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at.replace()
            storage.new(self)
            
    def save(self):
        """Updates the public instance attribute of updated_at"""
        self.updated_at = updated_at.utcnow()
        storage.save()
        
    def __str__(self):
        """Returns a string representation of the instanciated BaseModel"""
        name_of_class = self.__class__.__name
        return "[{}] ({}) {}".format(name_of_class, self.id, self.__dict__)
        
    def to_dict(self):
        """Returns a dictionary containing the values of the BaseModel"""
        my_inst_dic = self.__dict__.copy()
        my_inst_dic['created_at'] = self.created_at.isoformat()
        my_inst_dic['updated_at'] = self.updated_at.isoformat()
        my_inst_dic['__class__'] = self.__class__.__name
        return my_inst_dic