#!/usr/bin/python3

"""
11-student module.
"""


class Student(object):
    """
    Student class.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes an object.

        Args:
            first_name (str): The first name.
            last_name (str): The last name.
            age (int): The age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a student
            instance.

        Returns:
            dict: Representation of a student.
        """
        if type(attrs) is list:
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.

        Args:
            json (dict): JSON.
        """
        for k, v in json.items():
            if k in self.__dict__:
                self.__dict__[k] = v
