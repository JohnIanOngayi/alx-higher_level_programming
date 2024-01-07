#!/usr/bin/python3

"""

This module contains one function that adds two integers

"""


def add_integer(a, b=98):
    """

    Returns the integer sum of two numerics

    Args:
    a (int or float): the first numeric
    b (int or float and optional): the first numeric, defaults to 98

    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
