#!/usr/bin/python3

'''This module defines a Review class that
inherits from the basemodel class
'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''This class creates a Review
    '''

    place_id = ""
    user_id = ""
    text = ""
