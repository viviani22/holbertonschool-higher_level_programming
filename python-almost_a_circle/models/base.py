#!/usr/bin/python3
"""Task 1"""


class Base:
    """class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = id
