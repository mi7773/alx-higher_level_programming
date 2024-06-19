#!/usr/bin/python3

"""
0-read_file module.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The file name.
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        print(f.read(), end='')
