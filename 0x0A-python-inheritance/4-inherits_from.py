#!/usr/bin/python3

"""
4-inherits_from module.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class; otherwise False.

    Args:
        obj (any type): The object
        a_class (any_type): The class

    Returns:
        bool: True or False
    """
    if issubclass(type(obj), a_class) and not type(obj) is a_class:
        return True
    else:
        return False
