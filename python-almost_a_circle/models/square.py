#!/usr/bin/python3
"""Task 10.."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """subclass"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        if args and args != 0:
            list_arg = ["id", "size", "x", "y"]
            i = 0
            for num in args:
                setattr(self, list_arg[i], num)
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
