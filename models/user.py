#!/usr/bin/python3
"""This module defines a user model"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize User attributes and call the parent constructor"""
        super().__init__(*args, **kwargs)
