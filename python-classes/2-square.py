#!/usr/bin/python3
"""Task 2"""


class Square:
    """Class named Square"""
    def __init__(self, size=0):
        try:
            if type(size) is not int:
                raise TypeError
            if size < 0:
                raise ValueError
            self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
