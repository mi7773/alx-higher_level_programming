#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print('0 arguments.')
    elif len(argv) == 2:
        print('1 argument:')
    else:
        print('{:d} arguments:'.format(len(argv) - 1))
    for i in argv:
        if i == argv[0]:
            continue
        print('{:d}: {:s}'.format(argv.index(i), i))
