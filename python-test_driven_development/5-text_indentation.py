#!/usr/bin/python3
"""Task 5"""

def text_indentation(text):
    """ Prints new line after . ? or :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    indented_text = ""
    for i in range(len(text)):
        if text[i] == ' ' and text[i-1] in ['.', '?', ':']:
            continue
        indented_text += text[i]
        if text[i] in ['.', '?', ':'] and text[i+1] == ' ':
            indented_text += '\n' + '\n'
    print(indented_text)
