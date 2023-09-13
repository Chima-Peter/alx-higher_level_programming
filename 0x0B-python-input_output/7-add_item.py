#!/usr/bin/python3
"""
Module that uses save_to_json_file and load_from_json_file functions
"""
import sys
import json
import os.path
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

my_list = []
f = 'add_item.json'
if os.path.exists(f) is False:
    print("P")
    save(my_list, f)
my_list = load(f)
for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])
save(my_list, f)
