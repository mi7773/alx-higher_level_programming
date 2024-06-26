#!/usr/bin/python3

"""
0-add_integer module.
"""


def add_integer(a, b=98):
    """
    Adds 2 integers.

    Args:
        a (int): The first parameter.
        b (int, float): The second parameter.

    Returns:
        int: Sum of 2 integers.
    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    result = a + b
    if result == float('inf') or result == -float('inf'):
        raise OverflowError('cannot convert float infinity to integer')
    if result != result:
        raise ValueError('cannot convert float NaN to integer')
    return int(a) + int(b)
