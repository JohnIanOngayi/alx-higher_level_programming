#!/usr/bin/python3
"""

Module defines a class Square

"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Defines a square
    Subclass of class Rectangle
    """
    def __init__(self, size):
        """
        instantiates object of class Square
        """
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returns area of a square
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns informal string representation of object of class Square
        """
        return (f"[Square] {self.__size}/{self.__size}")
