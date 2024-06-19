#!/usr/bin/python3

"""
2-append_write module.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8)
        and returns the number of characters added.

    Args:
        filename (str): The file name.
        text (str): The text.

    Returns:
        int: The number of characters added.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        n = file.write(text)
    return n
