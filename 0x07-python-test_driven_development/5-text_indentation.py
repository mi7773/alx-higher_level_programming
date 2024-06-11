#!/usr/bin/python3

"""
5-text_indentation module.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters:
    ., ?, :

    Args:
        text (str): The first parameter.
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    for i in range(len(text)):
        if text[i] == ' ' and text[i - 1] in '.?:':
            pass
        else:
            print(text[i], end='')
        if text[i] in '.?:':
            print()
            print()
