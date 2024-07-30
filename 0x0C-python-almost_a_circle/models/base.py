#!/usr/bin/python3
""" base """
import json


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

    @classmethod
    def reset(cls):
        """ Resets nb_objects class attribute """
        cls.__nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: JSON representation.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        return json.dumps(list_dictionaries)
