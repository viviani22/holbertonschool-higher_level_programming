#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for element in matrix:
            for number in element:
                print("{:d}".format(number), end="")
                if number != element[-1]:
                    print(end=" ")
            print()
