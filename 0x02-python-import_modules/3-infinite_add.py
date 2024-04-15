#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    result = 0
    for i in argv:
        if i == argv[0]:
            continue
        result += int(i)
    print(f"{result:d}")
