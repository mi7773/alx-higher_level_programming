#!/usr/bin/python3

"""
2-is_same_class module.
"""


def is_same_class(obj, a_class):
    """
    Returns True is the object is exactly an instance of
        the specified class; otherwise False.

    Args:
        obj (any type): The object
        a_class (any type): The class

    Returns:
        bool: True or False
    """
    if type(obj) is a_class:
        return True
    else:
        return False
