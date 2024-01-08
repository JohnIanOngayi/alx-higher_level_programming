#!/usr/bin/python3
"""

Returns true if an object is na instance of class

"""


def inherits_from(obj, a_class):
    """
    Returns true if an object s an instance of a class
    """
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
