#!/usr/bin/python3
def uppercase(str):
    """prints a string in uppercase followed by a new line."""
    for c in str:
        i = ord(c)
        if i <= 122 and i >= 97:
            i -= 32
        print(f"{i:c}", end="")
    print(f"{10:c}", end="")
