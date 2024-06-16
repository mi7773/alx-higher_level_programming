#!/usr/bin/python3

"""
9-rectangle module.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Initializes objects.

        Args:
            width (int): The width.
            height (int): The height.
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self, *args):
        """
        Returns an inforaml and nicely printable string
            representation of a rectangle.

        Returns:
            str: String representation.
        """
        if args:
            self.__width = args[0]
            self.__height = args[1]
        return '[' + self.__class__.__name__ + '] ' + \
               str(self.__width) + '/' + str(self.__height)

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area.
        """
        return self.__width * self.__height
