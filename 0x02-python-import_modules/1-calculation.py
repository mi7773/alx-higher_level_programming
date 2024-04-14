#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    list_o = [add, sub, mul, div]
    list_s = ['+', '-', '*', '/']
    a = 10
    b = 5
    for i in list_o:
        print('{:d} {:s} {:d} = {:.0f}'.format(a, list_s[list_o.index(i)],
                                               b, i(a, b)))
