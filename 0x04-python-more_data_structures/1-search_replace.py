#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """replaces all occurrences of an element by another in a new list"""
    new_list = [i if i != search else replace for i in my_list]
    return new_list
