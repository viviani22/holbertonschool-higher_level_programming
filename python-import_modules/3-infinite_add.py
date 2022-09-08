#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 1
    sum_arg = 0
    while i != len(sys.argv):
        sum_arg += int(sys.argv[i])
        i += 1
    print("{}".format(sum_arg))
