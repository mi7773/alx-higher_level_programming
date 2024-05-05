#!/usr/bin/python3
def best_score(a_dictionary):
    """returns a key with the biggest integer value."""
    key = None
    value = 0
    if a_dictionary is not None:
        for k, v in a_dictionary.items():
            if v > value:
                value = v
                key = k
    return key
