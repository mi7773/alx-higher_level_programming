#!/usr/bin/python3

def safe_print_integer(value):
    """prints an integer with "{:d}".format()"""
    try:
        r = True
        print(F"{value:d}")
    except (ValueError, TypeError):
        r = False
    return r
