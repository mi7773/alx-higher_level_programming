#!/usr/bin/python3
import hidden_4
import os
if __name__ == "__main__":
    aa = dir(hidden_4)
    for a in aa:
        if a[0] != '_':
            print(a)
