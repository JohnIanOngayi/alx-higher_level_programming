#!/usr/bin/python3
"""

Module defines a class Rectangle

"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Defines a Rectangle
    Class Rectangle subclass of class BaseGeometry
    """
    def __init__(self, width, height):
        """
        Instantiates object of class Rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns area of object of class rectanglw
        """
        return self.__height * self.__width

    def __str__(self):
        """
        Returns an informal string representation of object of class Rectangle
        """
        return (f"[Rectangle] {self.__width}/{self.__height}")
