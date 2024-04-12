#!/usr/bin/python3

def print_last_digit(number):
    """prints the last digit of a number"""
    if number < 0:
        n = (number % -10) * -1
    else:
        n = number % 10
    print('{:d}'.format(n), end='')
    return n
