#!/usr/bin/python3
"""Task 1"""
import json


class Base:
    """class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """method"""
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        new_list = []
        if list_objs is not None:
            for obj in list_objs:
                new_list.append(obj.to_dictionary())
        with open(f"{cls.__name__}.json", "w") as file:
            file.write(cls.to_json_string(new_list))

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(1, 1)
        for key, value in dictionary.items():
            setattr(dummy, key, value)
        return dummy
