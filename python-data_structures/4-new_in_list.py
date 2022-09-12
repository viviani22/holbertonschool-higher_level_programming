#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return my_list
    new_list = list(my_list)
    for number in range(len(new_list)):
        if number == idx:
            new_list[number] = element
    return new_list
