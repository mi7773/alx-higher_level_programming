#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """prints a dictionary by ordered keys."""
    a_keys = list(a_dictionary.keys())
    a_keys.sort()
    for i in a_keys:
        print("{}: {}".format(i, a_dictionary[i]))
