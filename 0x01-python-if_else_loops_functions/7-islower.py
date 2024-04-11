#!/usr/bin/python3
def islower(c):
    """Checks for lowercase character."""
    i = ord(c)
    if i <= 122 and i >= 97:
        return 1
