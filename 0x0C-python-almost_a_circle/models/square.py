#!/usr/bin/python3
"""

Module defines  class Square that inherits from class Rectangle

"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines class Square from class Rectangle"""

    def __init__(self, size, x=0, y=0):
        """
        Instantiates object of class Square

        size(int and optional): side of sqaure, defaults to 0
        x(int and optional - inherited): horizontal offset, defaults to 0
        y(int and optional - inherited): vertical offset, defaults to 0
        """
        super().__init__(size, size, x, y, id=None)
        self.size = size

    def __str__(self):
        """
        Returns informal string representation of object
        """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")

    @property
    def size(self):
        """Returns size of object"""
        return self.__width

    @size.setter
    def size(self, value):
        """Sets size of object"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """Updates object attributes"""
        if args is not None and len(args) > 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(size, x, y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs is not None and len(kwargs) > 0:
            attr_list = ['id', 'size', 'x', 'y']
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key in attr_list and key != 'id':
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns dictionary representation of object"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
