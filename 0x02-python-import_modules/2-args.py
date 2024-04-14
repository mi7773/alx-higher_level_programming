#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    list_p = ['arguments.', 'argument:', 'arguments:']
    print('{:d} {:s}'.format(len(argv) - 1, list_p[1]
                             if len(argv) == 2 else list_p[0]
                             if len(argv) == 1 else list_p[2]))
    for i in argv:
        if i == argv[0]:
            continue
        print('{:d}: {:s}'.format(argv.index(i), i))
