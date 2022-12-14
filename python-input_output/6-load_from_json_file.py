#!/usr/bin/python3
"""Task 6"""
import json


def load_from_json_file(filename):
    """loads object from json file"""
    with open(filename, encoding="utf-8") as file:
        return json.loads(file.readline())
