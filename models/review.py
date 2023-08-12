#!/usr/bin/python3
from models.base_model import BaseModel

"""This is the Review modules"""


class Review(BaseModel):
    """
    This is the review class
    """
    
    place_id = ''
    user_id = ''
    text = ''
