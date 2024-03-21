#!/usr/bin/python

def print_sorted_dictionary(a_dictionary):
    keys_list = list(a_dictionary.keys())
    keys_list.sort()
    print({i: a_dictionary[i] for i in keys_list})
