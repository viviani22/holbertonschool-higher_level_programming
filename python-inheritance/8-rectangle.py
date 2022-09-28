#!/usr/bin/python3
"""Task 7"""
bg = __import__('7-base_geometry').BaseGeometry


class Rectangle(bg):
    """Class"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
