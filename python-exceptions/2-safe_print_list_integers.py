#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = 0
    for elem in my_list:
        try:
            if x > 0:
                if type(elem) == int:
                    print("{:d}".format(elem), end="")
                else:
                    continue
            else:
                break
            num += 1
            x -= 1
        except IndexError:
            break
    print()
    return num
