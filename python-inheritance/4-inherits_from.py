#!/usr/bin/python3
"""Task 4"""


def inherits_from(obj, a_class):
    """class"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
