#!/usr/bin/pyhton3

def no_c(my_string):
    ntext = ''
    nlist = []
    nlist += my_string
    for i in 'Cc':
        n = nlist.count(i)
        for j in range(n):
            nlist.remove(i)
    for i in nlist:
        ntext += i
    return ntext
