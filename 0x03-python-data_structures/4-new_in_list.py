#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    l = len(my_list)
    if idx < 0 or idx >= l:
        return my_list
    else:
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
