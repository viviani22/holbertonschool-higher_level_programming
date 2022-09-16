#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0
    for elem in my_list:
        try:
            if x > 0:
                print(f"{elem}", end="")
            else:
                break
            num += 1
            x -= 1
        except IndexError:
            break
    print()
    return num
