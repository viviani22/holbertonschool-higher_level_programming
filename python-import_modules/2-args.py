#!/usr/bin/python3
import sys
i = 1
if (len(sys.argv) > 1):
    print("{} arguments:".format(len(sys.argv) - 1))
else:
    print("0 arguments.")
while i != len(sys.argv):
    print("{}: {}".format(i, str(sys.argv[i])))
    i += 1
