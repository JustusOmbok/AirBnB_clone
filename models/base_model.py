#!/usr/bin/python3
from datetime import datetime
from models import storage
import uuid

class BaseModel:
    def __init__(self, *args, **kwargs):
        """"
        Initialises a base mode instance.
        """
        d = datetime.strptime
        if "id" not in kwargs:
            self.id = str(uuid.uuid4())
        else:
            self.id = kwargs['id']
        if "created_at" not in kwargs:
            self.created_at = datetime.now()
        else:
            self.created_at = d(kwargs["created_at"], '%Y-%m-%dT%H:%M:%S.%f')
        
        if "updated_at" not in kwargs:
            self.updated_at = self.created_at
        else:
            self.updated_at = d(kwargs["updated_at"], '%Y-%m-%dT%H:%M:%S.%f')
        
        if kwargs is not None and len(kwargs.items()) > 0:
            storage.new(self)
    
    def __str__(self):
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
        """ 
        returns string representation  of an instance
        """
    def save(self):
        """
    Updates the updated_at attribute and saves the instance
        """

        self.updated_at = datetime.now()
        dic = self.to_dict()
        storage.save()

    def all(cls):
        """ Returns a dictionary of all instances """
        return models.storage.all(cls)
    
    def to_dict(self):
        """
        Converts the instance to a dictionary representation 
        Returns a dictionary containing the attributes of the instance.
        """
        return {
            'id' : self.id,
            'created_at' : self.created_at.isoformat(),
            'updated_at' : self.updated_at.isoformat(),
            '__class__' : type(self).__name__
        }
