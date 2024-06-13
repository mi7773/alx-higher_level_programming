#!/usr/bin/python3

"""
2-rectangle module.
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
        Retrieves the width.

        Returns:
            int: The width value.
        """
        return self.__width

    @property
    def height(self):
        """
        Retrieves the height.

        Returns:
            int: The height value.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Sets the width value.

        Args:
            value (int): The width value.
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Sets the height value.

        Args:
            value (int): The height value.
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """
        Returns the rectangle area.

        Returns:
            int: The area of the rectangle.
        """
        return int(self.__width * self.__height)

    def perimeter(self):
        """
        Returns the rectangle perimeter.

        Returns:
            int: The perimeter of the rectangle.
        """
        if not self.__width or not self.__height:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
            for i in range(self.__height):
                for j in range(self.__width):
                    print('#', end='')
                if i < self.__height - 1:
                    print()
            return ''
