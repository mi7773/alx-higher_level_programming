#!/usr/bin/pyhton3

"""
1-rectangle module.
"""


class Rectangle(object):
    """
    Defines a rectangle.
    """
    def __init__(self, width, height):
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
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Sets height attribute.

        Args:
            Value (int): The value of height attribute.
        """
        self.__height = value
