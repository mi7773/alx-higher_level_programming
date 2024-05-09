#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """prints x elements of a list."""
    try:
        for i in range(x):
            print(my_list[i], end="")
    except IndexError:
        x = i
    print()
    return x
