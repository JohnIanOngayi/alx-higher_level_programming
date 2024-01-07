#!/usr/bin/python3
"""

This module prints a square with the character `#`

"""


def print_square(size) -> None:
    """

    Prints a square with the character `#`

    Args:
    size (int): the size length of the square

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        print("#" * size)
