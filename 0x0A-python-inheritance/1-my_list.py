#!/usr/bin/python3

"""
1-my_list module.
"""


class MyList(list):
    """
    Inherits from list.
    """
    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort).
        """
        print(sorted(self))
