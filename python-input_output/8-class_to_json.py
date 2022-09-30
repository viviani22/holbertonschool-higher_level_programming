#!/usr/bin/python3
import json
"""Task 8"""


def class_to_json(obj):
    """turns class to json"""
    return json.dumps(obj.__dict__)
