#!/usr/bin/python3
"""

This module prints a full name from a first and last name

"""


def say_my_name(first_name, last_name=""):
    """

    A function that prints a full name

    Args:
    first_name (str): the first name
    last_name (str and optional): the last name, defaults to empty string

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {0} {1}".format(first_name, last_name))
