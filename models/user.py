#!/usr/bin/python3

'''This module defines a User class that
inherits from the basemodel class
'''
from models.base_model import BaseModel


class User(BaseModel):
    '''This class creates a User
    '''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
