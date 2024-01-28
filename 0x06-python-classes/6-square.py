#!/usr/bin/python3
"""
Module defines a class square, its methods and object properties
"""


class Square:
    """
    Defines a square
    """

    def __init__(self, size: int = 0, position: tuple[int, int] = (0, 0)):
        """
        Initializes the Square class
        Args:
            size (int, optional): the size of the square. Defaults to 0.
            position (tuple, optional): coordinates of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self) -> int:
        """
        Retrieves the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value) -> None:
        """
        Sets or updates the size of the square
        Args:
            value (int): the size of the square
        """
        # size must be an integer
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        # it should be greater than or equal to zero
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self) -> tuple[int, int]:
        """
        Retrieves the 2-tuple containing the coordinates of the square
        Returns:
            tuple[int, int]: a 2-tuple containing the coordinates of the square
        """
        return self.__position

    @position.setter
    def position(self, value: tuple[int, int]) -> None:
        """
        Sets or updates the coordinates of the square
        Args:
            value (tuple[int, int]): a 2-tuple containing the
            coordinates of the square
        """
        # ensure we are receiving a 2-tuple
        if not isinstance(value, tuple) or len(value) < 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        # ensure each element in the 2-tuple is an integer as well
        if sum(1 for i in value if isinstance(i, int) and i >= 0) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def __custom_print_with_position(self) -> str:
        """
        Abstracts implementation of the 'my_print' function
        """
        if self.__position == 0:
            return "\n"  # there's nothing do here
        custom_str = "\n" * self.__position[1]  # update it with the height
        for _ in range(self.__size):
            custom_str += f"{' ' * self.__position[0]}{'#' * self.__size}\n"

        return custom_str

    def area(self) -> int:
        """
        Returns the area of the square
        """
        return self.__size**2

    def my_print(self) -> None:
        print(self.__custom_print_with_position()[:-1])
