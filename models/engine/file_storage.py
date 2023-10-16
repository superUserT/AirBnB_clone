#!/usr/bin/python3
"""This module defines the file storage"""
import json



class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return FileStorage.__objects
        else:
            filtered_objects = {}
            for object_id, obj in FileStorage.__objects.items():
                if isinstance(obj, cls):
                    filtered_objects[object_id] = obj
            return filtered_objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            for key, val in FileStorage.__objects.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists)."""
        from models.base_model import BaseModel
        from models.user import User
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for key, val in data.items():
                    class_name, obj_id = key.split('.')
                    if class_name == "User":
                        obj = User(**val)
                    elif class_name == "BaseModel":
                        obj = BaseModel(**val)
                    else:
                        continue
                    self.new(obj)
        except FileNotFoundError:
            pass
