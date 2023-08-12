#!/usr/bin/python3
import json
import os

"""" This our storage module. will convert files to JSON"""
class FileStorage:
    """
    This customer class for file storage
    """
    __file_path = "./file.json"
    __objects = {}

    def __init__(self) -> None:
        pass

    def all(self):
        """
        This function returns all objects in form of a disctionary
        """
        return self.__objects
    
    def new(self,obj):
        """
        adds new object to the storage dictionary
        """
        name = type(obj).__name__
        type(self).__objects[name + "." + str(obj.id)] = obj

    def save(self):
        """
        This serializes and  saves   objects in the dictionary to JSON file
        """
        temporary_dic = {f: s.to_dict() for f, s in type(self).__object.items()}
        with open(type(self).__file_path, "w+") as f:
            json.dump(temporary_dic, f)
    def reload(self):
        """
        Deserializes all objects from the JSON File
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review

        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                data = json.load(f)
            for key, value in data.items():
                class_name, obj_id = key.split(".")
                class_ = eval(class_name)
                obj = class_(**value)
                self.__objects[key] = obj