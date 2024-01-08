#!/usr/bin/python3
"""

Module returns true if an object is a subclass

"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class
    """
    return (type(obj) is a_class)
