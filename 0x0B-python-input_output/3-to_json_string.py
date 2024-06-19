#!/usr/bin/python3

"""
3-to_json_string module.
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj (any type): The object.

    Returns:
        str: The JSON representation.
    """
    return json.dumps(my_obj)
