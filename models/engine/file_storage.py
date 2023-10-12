import json
import os
import models.base_model

class FileStorage:
    __file_path = "file.json"  # Default path to the JSON file
    __objects = {}  # Dictionary to store serialized objects

    def all(self):
        """Return the dictionary of all objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Add a new object to the dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize and save the objects to the JSON file"""
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserialize objects from the JSON file"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                try:
                    deserialized_objects = json.load(file)
                    for key, obj_dict in deserialized_objects.items():
                        class_name, obj_id = key.split('.')
                        # Create instances based on class name and load the data
                        model_class = models.class_name_to_model[class_name]
                        obj = model_class(**obj_dict)
                        FileStorage.__objects[key] = obj
                except Exception:
                    pass

