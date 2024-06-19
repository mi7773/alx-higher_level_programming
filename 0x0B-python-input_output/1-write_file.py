#!/usr/bin/python3

"""
1-write_file module.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and
        returns the number of characters written.

    Args:
        filename (str): The file name.
        text (str): The text.

    Returns:
        int: The number of characters written.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        n = file.write(text)
    return n
