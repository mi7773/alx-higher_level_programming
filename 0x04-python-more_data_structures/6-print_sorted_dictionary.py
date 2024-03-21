#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    keys_list = list(a_dictionary.keys())
    keys_list.sort()
    sorted_a = {i: a_dictionary[i] for i in keys_list}
    for i in sorted_a:
        print(i, ':', a_dictionary[i])
