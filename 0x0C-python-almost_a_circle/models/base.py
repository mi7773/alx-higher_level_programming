#!/usr/bin/python3
""" base """


class Base(object):
    """ Base class """

    __nb_objects = 0
    """ int: The number of objects class attribute """

    def __init__(self, id=None):
        """
        Initializes instances.

        Args:
            id (int): The id value.
        """

        Base.__nb_objects += 1

        if id is None:
            self.id = Base.__nb_objects
            """ int: The id instance attribute """
        else:
            self.id = id
