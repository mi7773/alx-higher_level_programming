#!/usr/bin/python3

"""
9-student module.
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

    def to_json(self):
        """
        Retrieves a dictionary representation of a student
            instance.

        Returns:
            dict: Representation of a student.
        """
        return self.__dict__
