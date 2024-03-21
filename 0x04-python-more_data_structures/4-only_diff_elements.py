#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    od_set_1 = set()
    od_set_2 = set()
    od_set = set()
    n1 = len(set_1)
    n2 = len(set_2)
    if n1 > n2:
        od_Set_1 = set_1.copy()
        od_set = set_1.copy()
        od_set_2 = set_2.copy()
    else:
        od_set_1 = set_2.copy()
        od_set = set_2.copy()
        od_set_2 = set_1.copy()
    for i in od_set_1:
        for j in od_set_2:
            if i == j:
                od_set.remove(i)
                break
            else:
                od_set.add(j)
    return od_set
