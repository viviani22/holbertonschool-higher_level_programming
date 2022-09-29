#!/usr/bin/python3
"""Task 0"""


def read_file(filename=""):
    """func that reads file"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
