#!/usr/bin/python3

"""
0-add_integer module.
"""


def add_integer(a, b=98):
    """
    Adds 2 integers.

    Args:
        a (int): The first parameter.
        b (int): The second parameter.

    Returns:
        int: Sum of 2 integers.
    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return
    return int(a) + int(b)
