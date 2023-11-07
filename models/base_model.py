#!/usr/bin/python3

'''This module is the blue print for object creation
'''
from datetime import datetime, date
import uuid


class BaseModel:
    '''This is the model class blueprint
    '''
    def __init__(self, *rgs, **kwargs):
        '''This method creates an instance
        of the BaseModel Class'''
        if kwargs:
            del kwargs["__class__"]
            date_str_format = "%Y-%m-%dT%H:%M:%S.%f"
            kwargs["created_at"] = datetime.strptime(
                    kwargs["created_at"], date_str_format
                    )
            kwargs["updated_at"] = datetime.strptime(
                    kwargs["updated_at"], date_str_format
                    )
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        '''This is the user representation
        of objects'''

        obj_class_name = self.__class__.__name__
        obj_dict_rep = self.__dict__
        return ("[{}] ({}) {}".format(obj_class_name, self.id, obj_dict_rep))

    def save(self):
        '''Updates public instance attributes
        with the current time'''

        self.updated_at = datetime.now()

    def to_dict(self):
        '''Returns a dictionary containing all
        keys/values of __dict__ of the instance'''

        obj_dict = self.__dict__
        obj_dict["__class__"] = self.__class__.__name__
        created_to_str = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        obj_dict["created_at"] = created_to_str
        updated_to_str = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        obj_dict["updated_at"] = updated_to_str
        return obj_dict
