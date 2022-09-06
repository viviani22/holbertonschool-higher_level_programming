#!/usr/bin/python3
def uppercase(str):
    for c in range(len(str)):
        if ord(str[c]) > 96 and ord(str[c]) < 123:
            temp = chr(ord(str[c])-32)
        else:
            temp = str[c]
        if c != len(str) - 1:
            print("{}".format(temp), end="")
        else:
            print("{}".format(temp))

