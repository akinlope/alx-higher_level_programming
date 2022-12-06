#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 1:
        a1 = 0
        a0 = tuple_a[0]
    elif len(tuple_a) == 0:
        a0 = 0
        a1 = 0
    else:
        a1 = tuple_a[1]
        a0 = tuple_a[0]
    if len(tuple_b) == 1:
        b1 = 0
        b0 = tuple_b[0]
    elif len(tuple_b) == 0:
        b0 = 0
        b1 = 0
    else:
        b1 = tuple_b[1]
        b0 = tuple_b[0]
    return (a0 + b0, a1 + b1)
