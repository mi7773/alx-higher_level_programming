#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    i = len(my_list)
    if idx < 0 or idx >= i:
        return my_list
    my_list[idx] = element
    return my_list
