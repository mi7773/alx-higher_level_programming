#!/usr/bin/python3

"""
1-rectangle module.
"""


class Rectangle(object):
    """
    Defines a rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes objects.

        Args:
            width (int): Width of rectangle.
            height (int): Height of rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves width attribute.

        Returns:
            int: width value.
        """
        return self.__width

    @property
    def height(self):
        """
        Retrieves height attribute.

        Returns:
            int: height value.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Sets width attribute.

        Args:
            value (int): The value of width attribute.
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Sets height attribute.

        Args:
            Value (int): The value of height attribute.
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
