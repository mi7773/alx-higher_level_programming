#!/usr/bi/python3

def safe_print_list(my_list=[], x=0):
    """prints x elements of a list."""
    for i in range(x):
        try:
            print(my_list[i], end="")
        except:
            i -= 1
            break
    print()
    return i + 1
