#!/usr/bin/python3

"""
10-square module.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Inherits from Rectangle.
    """
    def __init__(self, size):
        """
        Initializes objects.

        Args:
            size (int): The size of square.
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: representation.
        """
        return super().__str__(self.__size, self.__size)
