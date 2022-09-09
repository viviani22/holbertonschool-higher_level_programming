#!/usr/bin/python3
import hidden_4
for strings in dir(hidden_4):
    if "__" not in strings:
        print(strings)
