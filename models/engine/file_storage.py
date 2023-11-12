#!/usr/bin/python3
'''This module details the file storage engine
of this AirBnB application'''
import json
import os.path


class FileStorage:
    '''This class serializes instances to a JSON
    string and stores them in a JSON file'''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''This method returns the __objects dictionary
        '''

        return self.__objects

    def new(self, obj):
        '''This method concatenates the object obj and it's id
        and sets in the __objects dictionary'''

        objects_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[objects_key] = obj

    def save(self):
        '''This method serializes all objects stored
        in the __objects dictionary to a JSON string
        and stores it in __file_path (i.e file.json)'''

        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(obj_dict, file)

    def reload(self):
        '''This method de-serializes the JSON file content
        back to a __objects dictionary if and only if it exists'''

        if os.path.isfile(FileStorage.__file_path):
            from models.base_model import BaseModel
            from models.user import User
            from models.state import State
            from models.city import City
            from models.amenity import Amenity
            from models.place import Place
            from models.review import Review
            '''add more imports as may be required for new classes'''

            class_mapping = {
                    'BaseModel': BaseModel, 'User': User, 'State': State,
                    'City': City, 'Amenity': Amenity, 'Place': Place,
                    'Review': Review
                    }
            '''add more class mappings as may be required for new classes'''

            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                deserialized_str = json.load(f)

                for obj_values in deserialized_str.values():
                    cls_name = obj_values["__class__"]

                    if isinstance(cls_name, str) and cls_name in class_mapping:
                        object_class = class_mapping[cls_name]
                        self.new(object_class(**obj_values))
