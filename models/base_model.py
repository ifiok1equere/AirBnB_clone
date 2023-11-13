#!/usr/bin/python3

'''This module is the blue print for object creation
'''
from datetime import datetime
import uuid
from models import storage


class BaseModel:
    '''This is the model class blueprint
    '''

    def __init__(self, *args, **kwargs):
        '''This method creates an instance
        of the BaseModel Class'''

        if kwargs:
            if "__class__" in kwargs.keys():
                del kwargs["__class__"]
            kwargs["created_at"] = datetime.fromisoformat(kwargs["created_at"])
            kwargs["updated_at"] = datetime.fromisoformat(kwargs["updated_at"])
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        '''This is the user representation
        of objects'''

        obj_class_name = self.__class__.__name__
        obj_dict_rep = self.__dict__
        return ("[{:s}] ({:s}) {}".format(
            obj_class_name, self.id, obj_dict_rep)
            )

    def __repr__(self):
        """Return the string representation of the instance."""

        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__
                )

    def save(self):
        '''Updates public instance attributes
        with the current time'''

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''Returns a dictionary containing all
        keys/values of __dict__ of the instance'''

        obj_dict = {}
        obj_dict = self.__dict__
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()

        return obj_dict
