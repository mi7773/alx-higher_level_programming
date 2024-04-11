#!/usr/bin/python3
def uppercase(str):
    """prints a string in uppercase followed by a new line."""
    for c in str:
        i = ord(c)
        if i <= 122 and i >= 97:
            i -= 32
        print("{:c}".format(i), end="")
    print()
