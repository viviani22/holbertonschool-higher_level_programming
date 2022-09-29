#!/usr/bin/python3
"""Task 5"""
import json


def save_to_json_file(my_obj, filename):
    """writes object to text files"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
