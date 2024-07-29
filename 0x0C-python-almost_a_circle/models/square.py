#!/usr/bin/python3
""" square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """"Square class """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes instances.

        Args:
            size (int): The size value.
            x (int): The x value.
            y (int): The y value.
            id (int): The id value.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return Square.width.fget(self)

    @size.setter
    def size(self, value):
        Rectangle.width.fset(self, value)
        Rectangle.height.fset(self, value)
