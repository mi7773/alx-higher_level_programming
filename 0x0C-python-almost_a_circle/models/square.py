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
        # super(Square, self).__init__(size, size, x, y, id)
        # super(Square, Square).__init__(self, size, size, x, y, id)
        # Rectangle.__init__(self, size, size, x, y, id)
        # Square.__init__(self, size, size, x, y, id)  # fails

    def __str__(self):
        """ Draft """
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.size}'

    @property
    def size(self):
        return super().width
        # return super().width.fget(self)  # fails
        # return super().width.__get__()  # fails
        # return Square.width.__get__(self)
        # return Rectangle.width.__get__(self)
        # return Square.width.fget(self)
        # return Rectangle.width.fget(self)

    @size.setter
    def size(self, value):
        super().__init__(value, value, self.x, self.y, self.id)
        # super().width = value  # fails
        # super(Square, Square).width.fset(self, value)
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

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle.

        Returns:
            dict: Representation of a Rectangle.
        """
        # super().to_dictionary()
        return {
                'size': self.size,
                'id': self.id,
                'x': self.x,
                'y': self.y
                }
