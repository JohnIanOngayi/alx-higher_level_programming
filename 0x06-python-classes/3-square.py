#!/usr/bin/python3

"""A class defininng a square"""


class Square:
    """A class defininng a square"""
    def __init__(self, size=0):
        """
        Constructs a square
        Args:
        size (int): The side of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2
