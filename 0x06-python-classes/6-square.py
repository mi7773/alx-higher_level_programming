#!/usr/bin/python3

"""
Contains a Square class.
"""


class Square(object):
    """
    Defines a square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes objects.

        Args:
            size (int): Size of the square,
                it must be integer and >= 0,
                equals 0 if it is not given.

            position (tuple): Must be a tuple of 2 positive integers
        """
        self.__size = size
        self.__position = position

    def area(self):
        """
        Returns the current square area.

        Returns:
            The current square area.
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        size property
        """
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """
        position property
        """
        return self.__position

    @position.setter
    def position(self, position):
        if type(position) is not tuple or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def my_print(self):
        """
        Prints in stdout the square with character #.
        """
        for j in range(self.__size):
            for i in range(self.__position[0]):
                print(" ", end="")
            for i in range(self.__size):
                print('#', end='')
            print()
        if self.__size == 0:
            print()
