#!/usr/bin/python3
"""
Module inherits from list
"""


class MyList(list):
    """
    Inherits from list and returns sorted list
    """
    def print_sorted(self):
        """
        Prints a sorted list
        """
        print(sorted(self))
