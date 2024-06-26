#!/usr/bin/python3

"""
5-save_to_json_file module.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file,
        using a JSON representation.

    Args:
        my_obj (any tybe): The object.
        filename: The file name.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(json.dumps(my_obj))
