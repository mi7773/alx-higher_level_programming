#!/usr/bin/python3

def no_c(my_string):
    """removes all characters c and C from a string."""
    n_string = ''
    for i in my_string:
        if i != 'c' and i != 'C':
            n_string += '{:s}'.format(i)
    return n_string
