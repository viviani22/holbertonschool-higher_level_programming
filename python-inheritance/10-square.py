#!/usr/bin/python3
"""Task 10"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        return super().area()
