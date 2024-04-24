#!/usr/bin/python3

def multiple_returns(sentence):
    """returns a tuple with the length of a string and its first character."""
    result = (len(sentence), None if len(sentence) == 0 else sentence[0])
    return result
