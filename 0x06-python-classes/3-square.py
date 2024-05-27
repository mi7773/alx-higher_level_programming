#!/usr/bin/python3

"""
Contains a Square class.
"""


class Square(object):
    """
    Defines a square.
    """
    def __init__(self, size=0):
        """
        Initializes objects.

        Args:
            size: Size of the square,
                it must be integer and >= 0,
                equals 0 if it is not given.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns the current square area.
        
        Returns:
            The current square area.
        """
        return self.__size ** 2
