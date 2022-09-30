#!/usr/bin/python3
"""task 7"""
import sys
import os
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

old_arg = []
if os.path.exists("add_item.json"):
    old_arg = load_from_json_file("add_item.json")
arguments = old_arg + sys.argv[1:]
save_to_json_file(arguments, "add_item.json")
