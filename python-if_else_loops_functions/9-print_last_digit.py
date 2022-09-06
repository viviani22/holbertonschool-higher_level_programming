#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        temp = (number % -10) * -1
    else:
        temp = number % 10
    print("{}".format(temp), end="")
    return temp
