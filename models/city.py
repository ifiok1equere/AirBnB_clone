#!/usr/bin/python3

'''This module defines a City class that
inherits from the basemodel class
'''
from models.base_model import BaseModel


class City(BaseModel):
    '''This class creates a City
    '''

    state_id = ""
    name = ""
