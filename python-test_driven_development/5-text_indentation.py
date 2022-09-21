#!/usr/bin/python3
"""Task 5"""


def text_indentation(text):
    """ Prints new line after . ? or :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    indented_text = ""
    for i in range(len(text)):
        if text[i] == ' ' and flag == 1:
            continue
        flag = 0
        indented_text += text[i]
        if text[i] in ['.', '?', ':']:
            indented_text += '\n' + '\n'
            flag = 1
    print(indented_text, end="")
