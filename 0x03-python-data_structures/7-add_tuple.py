#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """adds 2 tuples."""
    result = [0, 0]
    for i in range(2):
        for t in [tuple_a, tuple_b]:
            if len(t) >= i + 1 and t is not None:
                result[i] += t[i]
    return tuple(result)
