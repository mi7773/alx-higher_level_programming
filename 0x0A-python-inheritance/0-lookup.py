#!/usr/bin/python3

"""
0-lookup module.
"""


def lookup(obj):
    """
    Returns the list of available attributes
        and methods of an object.

    Args:
        obj (object): The object.

    Returns:
        list: A list of attributes and methods.
    """
    return dir(obj)
