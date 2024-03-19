#!/usr/bin/python3

def no_c(my_string):
    r = -1
    n = 0
    for l in my_string:
        r += 1
        if l == "c" or l == 'C':
             print(my_string[n:r], end="")
             n = r + 1
    print()
