#!/usr/bin/python3
from models.base_model import BaseModel
"""
This is the user module
"""


class User(BaseModel):
    """"
    User class
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def count(cls):
        """ Returns number of instances """
        return len(models.storage.all(cls))
    
