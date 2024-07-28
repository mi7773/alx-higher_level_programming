#!/usr/bin/python3
""" rectangle """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes instances.

        Args:
            width (int): The width value.
            height (int): The height value.
            x (int): The x value.
            y (int): The y value.
            id (int): The id value.
        """

        super().__init__(id)
        self.__width = width
        """ int: The width instance attribute """
        self.__height = height
        """ int: The height instance attribute """
        self.__x = x
        """ int: The x instance attribute """
        self.__y = y
        """ int: the y instance attribute """

    @property
    def width(self):
        """
        Returns the width of the instance.

        Returns:
            int: The width of the instance.
        """
        return self.__width

    @property
    def height(self):
        """
        Returns the height of the instance.

        Returns:
            int: The height of the instance.
        """
        return self.__height

    @property
    def x(self):
        """
        Returns the x of the instance.

        Returns:
            int: The x of the instance.
        """
        return self.__x

    @property
    def y(self):
        """
        Returns the y of the instance.

        Returns:
            int: The y of the instance.
        """
        return self.__y

    @width.setter
    def width(self, value):
        """
        Sets the value of the instance width.

        Args:
            value (int): The new width value.
        """
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Sets the value of the instance height.

        Args:
            value (int): The new height value.
        """
        self.__height = value

    @x.setter
    def x(self, value):
        """
        Sets the value of the instance x.

        Args:
            value (int): The new x value.
        """
        self.__x = value

    @y.setter
    def y(self, value):
        """
        Sets the value of the instance y.

        Args:
            value (int): The new y value.
        """
        self.__y = value
