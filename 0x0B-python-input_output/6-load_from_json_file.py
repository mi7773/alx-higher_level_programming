#!/usr/bin/python3

"""
6-load_from_json_file module.
"""

import json


def load_from_json_file(filename):
    """
    Creates an Object from a "JSON file".

    Args:
        filename (str): The file name.

    Returns:
        ant type: The object.
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        text = file.read()
    return json.loads(text)
