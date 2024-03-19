#!/usr/bin/pyhton3

def no_c(my_string):
    n = -1
    new_string = my_string
    for c in new_string:
        n += 1
        if c == 'c' or c == 'C':
            new_string[n:n + 1] = []
    print(new_string)
