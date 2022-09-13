#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_list = []
    for element1 in set_1:
        if element1 not in set_2:
            new_list.append(element1)
    for element2 in set_2:
        if element2 not in set_1:
            new_list.append(element2)
    return set(new_list)
