#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if (len(sys.argv) != 3):
        exit(1)
    a = int(str(sys.argv[1]))
    op = str(sys.argv[2])
    b = int(str(sys.argv[3]))
    if (op == "+"):
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif (op == "-"):
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif (op == "*"):
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif (op == "/"):
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
