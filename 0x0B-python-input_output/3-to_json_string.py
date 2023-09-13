#!/usr/bin/python3
"""
Module that creates the to_json_string fucntion
"""
import json


def to_json_string(my_obj):
    """
    A function that returns the JSON representation of an object
    """
    return json.dumps(my_obj)
