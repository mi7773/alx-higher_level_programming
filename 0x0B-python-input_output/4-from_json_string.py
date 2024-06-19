#!/usr/bin/python3

"""
4-from_json_string module.
"""

import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure)
        represented by a JSON string.

    Args:
        my_str (str): JSON string.

    Returns:
        any type: Pyhton data structure.
    """
    return json.loads(my_str)
