#!/usr/bin/python3
def weight_average(my_list=[]):
    weighted_sum = 0
    divider = 0
    for pair in my_list:
        divider += pair[1]
        weighted_sum += (pair[0] * pair[1])
    return weighted_sum / divider

