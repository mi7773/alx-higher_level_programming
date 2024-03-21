#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    temp = set_1.copy()
    od_set = set_1.copy()
    for i in set_2:
        for j in temp:
            if i == j:
                od_set.remove(i)
                break
            od_set.add(i)
    return od_set
