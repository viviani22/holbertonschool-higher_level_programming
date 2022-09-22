#!/usr/bin/python3
"""Task 9"""


class Rectangle:
    """class for rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

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
        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__height * 2 + self.__width * 2

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        string = ""
        for i in range(self.__height):
            for j in range(self.__width):
                string += str(self.print_symbol)
            if i != self.__height - 1:
                string += '\n'
        return string

    def __repr__(self):
        return(f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1

    @classmethod
    def square(cls, size=0):
        if type(size) is not int:
            raise TypeError()
        return cls(size, size)
