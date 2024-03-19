#!/usr/bin/pyhton3

def no_c(my_string):
    new_string = my_string[:]
    for c in new_string:
        if c == 'c' or c == 'C':
            n = index(c)
            new_string[n:n + 1] = []
    print(new_string)
