#!/usr/bin/python3

"""
3-say_my_name module.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first name> <last name>

    Args:
        first_name (str): The first parameter
        last_name (str): The second parameter

    Returns:
        str: The return of the function
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print(f'My name is {first_name} {last_name}')
