#!/usr/bin/python3
"""
This is the module for the user class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    This is the user class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
