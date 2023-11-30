#!/usr/bin/python3

import sys

if __name__ == "__main__":

    num = len(sys.argv)

    if num == 1:
        print("0 arguments.")

    elif num == 2:
        print("1 argument:")

        for i in range(1, len(sys.argv)):
            print("{0:d}: {1}".format(i, sys.argv[i]))

    else:
        print("{0:d} arguments:".format(len(sys.argv) - 1))

        for i in range(1, len(sys.argv)):
            print("{0:d}: {1}".format(i, sys.argv[i]))
