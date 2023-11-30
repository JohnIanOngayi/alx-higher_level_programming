#!/usr/bin/python3

import sys

num = len(sys.argv)

if num < 2:
    print("0 arguments.")

else:
    print("{0:d} arguments:".format(len(sys.argv) - 1))

    for i in range(1, len(sys.argv)):
        print("{0:d}: {1}".format(i, sys.argv[i]))
