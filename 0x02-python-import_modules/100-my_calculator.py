#!/usr/bin/python3

import sys

from calculator_1 import add, sub, mul, div

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        op = sys.argv[2]

        if sys.argv[2] not in "+-*/":
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)

        elif sys.argv[2] == "+":
            print("{0:d} {1} {2:d} = {3:d}".format(a, op, b, add(a, b)))

        if sys.argv[2] == "-":
            print("{0:d} {1} {2:d} = {3:d}".format(a, op, b, sub(a, b)))

        if sys.argv[2] == "*":
            print("{0:d} {1} {2:d} = {3:d}".format(a, op, b, mul(a, b)))

        if sys.argv[2] == "/":
            print("{0:d} {1} {2:d} = {3:d}".format(a, op, b, div(a, b)))
