#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = my_list[:]
    result = 0
    for n in new_list:
        m = new_list.count(n)
        if m > 1:
            while m > 1:
                new_list.remove(n)
                m -= 1
    for n in new_list:
        result += n
    return result
