#!/usr/bin/python3
"""Task 4"""


class Rectangle:
    """class for rectangle"""
    def __init__(self, width=0, height=0):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

    @height.setter
    def height(self, height):
        self.__height = height
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height is 0 or self.__width is 0:
            return 0
        return self.__height * 2 + self.__width * 2

    def __str__(self):
        if self.__height is 0 or self.__width is 0:
            return ""
        string = ""
        for i in range(self.__height):
            for j in range(self.__width):
                string += '#'
            if i != self.__height - 1:
                string += '\n'
        return string

    def __repr__(self):
        return(f"Rectangle({self.__width}, {self.__height})")
