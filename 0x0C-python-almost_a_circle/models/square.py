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
        return super().width
        # return super().width.fget(self) # fails
        # return super().width.__get__() # fails
        # return Square.width.__get__(self)
        # return Rectangle.width.__get__(self)
        # return Square.width.fget(self)
        # return Rectangle.width.fget(self)

    @size.setter
    def size(self, value):
        # super().width = value # fails
        super(Square, Square).width.fset(self, value)
        # super(Square, Square).width.__set__(self, value)
        # Square.width.fset(self, value)
        # Rectangle.width.fset(self, value)
        # Square.width.__set__(self, value)
        # Rectangle.width.__set__(self, value)

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute.

        Args:
            args (tuple): The arguments.
            kwargs (dict): The arguments.
        """
        super().update(*args, **kwargs)
