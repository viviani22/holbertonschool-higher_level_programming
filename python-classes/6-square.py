#!/usr/bin/python3
"""Task 6"""


class Square:
    """Class named Square"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__position = position
        if len(position) != 2 or\
                type(position[0]) is not int or type(position[1]) is not int\
                or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position
        if len(position) != 2 or\
                type(position[0]) is not int or type(position[1]) is not int\
                or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    @size.setter
    def size(self, size):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size**2

    def my_print(self):
        if self.__size <= 0:
            print()
        new_lines = int(self.__position[1])
        while new_lines != 0 and self.__size != 0:
            print()
            new_lines -= 1
        for i in range(self.__size):
            spaces = int(self.__position[0])
            while spaces > 0:
                print(end=" ")
                spaces -= 1
            for j in range(self.__size):
                print("#", end="")
            print()
