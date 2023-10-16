#!/usr/bin/python3
"""This module defines a city model"""
from models.base_model import BaseModel


class City(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        state_id = " "
        name = " "
