#!/usr/bin/python3
def uppercase(str):
    """prints a string in uppercase followed by a new line."""
    # str[0] = 'i' we can't since strings in Python are immutable.
    new_string = ""
    for c in str:
        i = ord(c)
        if i <= 122 and i >= 97:
            i -= 32
        new_string += chr(i)
    print("{:s}".format(new_string))
