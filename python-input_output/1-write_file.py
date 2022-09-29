#!/usr/bin/python3
"""Task 1"""


def write_file(filename="", text=""):
    """returns nr of char written"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        characters = 0
        for char in text:
            characters += 1
        return characters
