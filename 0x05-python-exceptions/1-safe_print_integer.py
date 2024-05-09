#!/usr/bin/python3

def safe_print_integer(value):
    """prints an integer with "{:d}".format()"""
    try:
        r = True
        result = value + 0
        print(value)
    except TypeError:
        r = False
    return r
