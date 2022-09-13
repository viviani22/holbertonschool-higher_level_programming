#!/usr/bin/python3
def best_score(a_dictionary):
    max_value = 0
    best_key = ""
    if a_dictionary:
        for key in a_dictionary:
            if max_value < a_dictionary[key]:
                max_value = a_dictionary[key]
                best_key = key
        return best_key
    return None
