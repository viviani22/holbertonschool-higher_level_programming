#!/usr/bin/python3
"""Task 2"""


def append_write(filename="", text=""):
    """appends at end of file"""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
        characters=0
        for char in text:
            characters+=1
        return characters
