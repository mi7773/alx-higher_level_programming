#!/usr/bin/python3

def no_c(my_string):
    r = -1
    for l in my_string:
        r += 1
        if l == "c" or l == 'C':
             break
    print(my_string[:r], my_string[r + 1:])
