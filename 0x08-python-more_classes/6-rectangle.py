#!/usr/bin/python3

"""
2-rectangle module.
"""


class Rectangle(object):
    """
    Defines a rectangle.

    Attributes:
        number_of_instances (int): Total number of rectangles.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes objects.

        Args:
            width (int): Width of rectangle.
            height (int): Height of rectangle.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        """
        Represents the rectangle with the character #.

        Returns:
            str: An informal and nicely printable string
                representation of a rectangle.
        """
        if not self.__width or not self.__height:
            return ''
        rectangle = []
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append('#')
            if i < self.__height - 1:
                rectangle.append('\n')
        return ''.join(rectangle)

    def __repr__(self):
        """
        Returns a string representation of the rectangle
        to be able to recreate a new instance by using eval().

        Returns:
            str: An official string representation of a rectangle.
        """
        return 'Rectangle(' + str(self.__width) +\
               ', ' + str(self.__height) + ')'

    def __del__(self):
        """
        Deletes a rectangle.
        """
        type(self).number_of_instances -= 1
        print('Bye rectangle...')
