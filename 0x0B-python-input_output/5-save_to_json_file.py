#!/usr/bin/python3
"""
Module that creates the save_to_json_file funnction
"""
import json


def save_to_json_file(my_obj, filename):
    """
    A function that writes an Object to a text file,\
            using a JSON representation:
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.load(my_obj, f)
