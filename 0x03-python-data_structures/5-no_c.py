#!/usr/bin/python3

def no_c(my_string):
    """removes all characters c and C from a string."""
    new_string = list(my_string)
    n_string = ''
    for i in new_string:
        if i != 'c' and i != 'C':
            n_string += '{:s}'.format(i)
    return n_string
