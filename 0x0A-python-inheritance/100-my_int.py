#!/usr/bin/python3
"""
Module defines a class MyInt
"""


class MyInt(int):
    """
    Rebel subclass of standard class int
    """
    def __ne__(self, other):
        return (not self < other and not self > other)

    def __eq__(self, other):
        return (self < other or self > other)
