#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                        'C': 100, 'D': 500, 'IV': 4, 'IX': 9, 'XL': 40,
                        'XC': 90, 'CD': 400}
    if not type(roman_string) == str or roman_string is None:
        return 0
    i = 0
    decimal_number = 0
    while i < len(roman_string):
        if roman_string[i:i+2] in roman_dictionary:
            decimal_number += roman_dictionary[roman_string[i:i+2]]
            i += 2
        elif roman_string[i] in roman_dictionary:
            decimal_number += roman_dictionary[roman_string[i]]
            i += 1
    return decimal_number
