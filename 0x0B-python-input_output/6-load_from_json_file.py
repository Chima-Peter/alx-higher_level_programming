#!/usr/bin/python3
"""
Module that creates the load_from_json_file function
"""
import json


def load_from_json_file(filename):
    """
    A function that creates an Object from a “JSON file”
    """
    with open(filename, 'r', encoding='utf-8') as f:
        json.load(f)
