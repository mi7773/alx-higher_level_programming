#!/usr/bin/python3
import sys
n = len(sys.argv) - 1
print(n, end=" ")
if n == 0:
    print("arguments.")
elif n == 1:
    print("argument:")
else:
    print("arguments:")
if n > 0:
    for i in range(1, n+1):
        print("{:d}: {}".format(i, sys.argv[i]))
