#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    l_a = len(tuple_a)
    l_b = len(tuple_b)
    if l_a == 0:
        a0 = 0
        a1 = 0
    elif l_a == 1:
        a0 = tuple_a[0]
        a1 = 0
    else:
        a0 = tuple_a[0]
        a1 = tuple_a[1]

    if l_b == 0:
        b0 = 0
        b1 = 0
    elif l_b == 1:
        b0 = tuple_b[0]
        b1 = 0
    else:
        b0 = tuple_b[0]
        b1 = tuple_b[1]

    reslt = (a0 + b0, a1 + b1)
    return(reslt)
