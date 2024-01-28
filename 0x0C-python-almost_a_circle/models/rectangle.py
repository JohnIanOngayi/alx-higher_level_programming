#!/usr/bin/python3
"""

Module creates class Rectangle that inherits from Base

"""
from models.base import Base


class Rectangle(Base):
    """
    Subclass of base defines a rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instantates object of class Rectangle

        width: width
        height: height
        x: horizontal offset
        y: vertical offset

        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Returns width of object"""
        return self.__width

    @property
    def height(self):
        """Returns height of object"""
        return self.__height

    @property
    def x(self):
        """Returns horizontal offset of object"""
        return self.__x

    @property
    def y(self):
        """Returns vertical offset of object"""
        return self.__y

    @width.setter
    def width(self, value):
        """Sets width of object"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets height of object"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Sets horizontal offset of object"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value


    @y.setter
    def y(self, value):
        """Sets vertical offset of object"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area of object"""
        return (self.__width * self.__height)

    def display(self):
        """Displays Rectangle with #"""
        for j in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Returns informal str representation of objet"""
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} "
                f"- {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """Assigns argument to each attribute"""
        a = 0
        if args is not None and len(args) > 0:
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs is not None and len(kwargs) > 0:
            attr_tuple = ('id', 'width', 'height', 'x', 'y')
            for key, value in kwargs.items():
                if key == 'id':
                    if value is None:
                        self.__init__(width, height, x, y)
                    else:
                        self.id = value
                elif key in attr_tuple and key != 'id':
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns dictionary reprecsentation for Rectangle object"""
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
