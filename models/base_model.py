#!/usr/bin/python3
from datetime import datetime
import uuid

class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        Initializes a base model instance.
        """
        if "id" not in kwargs:
            self.id = str(uuid.uuid4())
        else:
            self.id = kwargs['id']
        if "created_at" not in kwargs:
            self.created_at = datetime.now()
        else:
            self.created_at = datetime.strptime(kwargs["created_at"], '%Y-%m-%dT%H:%M:%S.%f')
        
        if "updated_at" not in kwargs:
            self.updated_at = self.created_at
        else:
            self.updated_at = datetime.strptime(kwargs["updated_at"], '%Y-%m-%dT%H:%M:%S.%f')
        
    def __str__(self):
        """
        Returns string representation of an instance.
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
        
    def save(self):
        """
        Updates the updated_at attribute and saves the instance.
        """
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """
        Converts the instance to a dictionary representation.
        """
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            '__class__': type(self).__name__
        }

if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    
    my_model.save()
    print(my_model)
    
    my_model_json = my_model.to_dict()
    print(my_model_json)
    
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
