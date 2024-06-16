#!/usr/bin/python3

"""
5-base_geometry module.
"""


class BaseGeometry(object):
    """
    BaseGeometry class.
    """

    def area(self):
        """
        Raises an Exception with the message area() is not implemented.
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validates value.

        Args:
            name (str): The name.
            value (int): The value.
        """
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
