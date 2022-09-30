#!/usr/bin/python3
"""Task 9"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        dictionary = {}
        if "first_name" in attrs:
            dictionary["first_name"] = self.first_name
        if "last_name" in attrs:
            dictionary["last_name"] = self.last_name
        if "age" in attrs:
            dictionary["age"] = self.age
        return dictionary

    def reload_from_json(self, json):
        if json:
            self.first_name = json["first_name"]
            self.last_name = json["last_name"]
            self.age = json["age"]
