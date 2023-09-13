#!/usr/bin/python3
"""
Module that uses save_to_json_file and load_from_json_file functions
"""
import sys
import json
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file
import os.path

is os.path.exists('add_item.json') is False:
    print("Error")
