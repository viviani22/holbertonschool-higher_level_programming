#!/usr/bin/python3
"""Task 12"""


def pascal_triangle(n):
    big_list = []
    i = 0
    for i in range(n):
        j = 0
        small_list = []
        for j in range(i + 1):
            if i > 1 and j != i and j > 0:
                small_list.append(big_list[i - 1][j] + big_list[i - 1][j - 1])
            else:
                small_list.append(1)
        big_list.append(small_list)
    return big_list
