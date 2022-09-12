#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = tuple_a + (0, 0)
    new1_tuple = tuple_b + (0, 0)
    result_tuple = new_tuple[0] + new1_tuple[0], new_tuple[1] + new1_tuple[1]
    return result_tuple
