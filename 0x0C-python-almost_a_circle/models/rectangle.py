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
        self.width = width
        """ int: The width instance attribute """
        self.height = height
        """ int: The height instance attribute """
        self.x = x
        """ int: The x instance attribute """
        self.y = y
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

        Raises:
            TypeError: If width is not int.
            ValueError: If width is not > 0.
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """
        Sets the value of the instance height.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If height is not int.
            ValueError: If height is not > 0.
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @x.setter
    def x(self, value):
        """
        Sets the value of the instance x.

        Args:
            value (int): The new x value.

        Raises:
            TypeError: If x is not int.
            ValueError: If x is not >= 0.
        """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        """
        Sets the value of the instance y.

        Args:
            value (int): The new y value.

        Raises:
            TypeError: If y is not int.
            ValueError: If y is not >= 0.
        """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    @classmethod
    def reset(cls):
        """ Resets nb_objects class attribute """
        Base.reset()

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """ Prints in stdout the rectangle instance with the character # """
        r = []
        r.append('\n' * self.y)
        for i in range(self.height):
            r.append(' ' * self.x)
            for j in range(self.width):
                r.append('#')
            r.append('\n')
        print(''.join(r), end='')

    def __str__(self):
        """
        Returns string representation.

        Returns:
            str: An informal and nicely printable string
                representation of an instance.
        """
        if self.width == self.height:
            return f'[{self.__class__.__name__}] ({self.id}) \
{self.x}/{self.y} - {self.width}'
        return f'[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} - \
{self.width}/{self.height}'

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute.

        Args:
            args (tuple): The arguments.
        """
        if self.width == self.height:
            attr = ['id', 'size', 'x', 'y']
        else:
            attr = ['id', 'width', 'height', 'x', 'y']
        i = 0
        for arg in args:
            if self.width == self.height and i == 1:
                setattr(self, 'height', arg)
            setattr(self, attr[i], arg)
            i += 1
        if len(args) == 0:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'height', value)
                setattr(self, key, value)
