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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances.
        """
        with open(f'{cls.__name__}' + '.json', 'w') as file:
            if list_objs is None:
                file.write('[]')
            else:
                lis = []
                for ins in list_objs:
                    lis.append(cls.to_dictionary(ins))
                r = Base.to_json_string(lis)
                file.write(r)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string.

        Args:
            json_string (str): JSON string representation.

        Returns:
            list: The list of the JSON string representation.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.

        Args:
            **dictionary: Arbitrary keyword arguments.

        Returns:
            An instance.
        """
        if cls.__name__ == 'Rectangle':
            ins = cls(1, 1)
        else:
            ins = cls(1)
        ins.update(**dictionary)
        return ins

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances.

        Returns:
            list: A list of instances.
        """
        try:
            with open(f'{cls.__name__}.json', 'r') as file:
                json_string = file.read()
                lis_dic = cls.from_json_string(json_string)
                lis_ins = []
                for dic in lis_dic:
                    ins = cls.create(**dic)
                    lis_ins.append(ins)
        except Exception:
            lis_ins = []
        finally:
            return lis_ins
