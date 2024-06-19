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
    write_file = __import__('1-write_file').write_file
    text = json.dumps(my_obj)
    write_file(filename, text)
