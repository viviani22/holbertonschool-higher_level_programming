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

    def from_json_string(json_string):
        """method"""
        new_list = []
        if json_string is not None:
            new_list += json.loads(json_string)
        return new_list

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        new_list = []
        with open(f"{cls.__name__}.json") as file:
            json_list = cls.from_json_string(file.read())
            for instance in json_list:
                new_list.append(cls.create(**instance))
        return new_list
