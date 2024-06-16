#!/usr/bin/python3

"""
8-rectangle module.
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
