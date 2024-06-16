#!/usr/bin/python3

"""
3-is_kind_of_class module.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of,
        or if the object is an instance of a class
        that inherited from, the specified class;
        otherwise False.

    Args:
        obj (any type): The object
        a_class (any_type): The class

    Returns:
        bool: True or False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
