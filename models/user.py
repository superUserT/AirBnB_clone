#!/usr/bin/python3
"""This module defines a user model"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initialize User attributes"""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

    def __str__(self):
        """Return a string representation of User instance"""
        return "[User] ({}) {}".format(self.id, self.__dict__)