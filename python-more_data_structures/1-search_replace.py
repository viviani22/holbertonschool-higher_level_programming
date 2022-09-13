#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for number in range(len(new_list)):
        if new_list[number] == search:
            new_list[number] = replace
    return(new_list)
