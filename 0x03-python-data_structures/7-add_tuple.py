#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_0 = tuple_a + (0, 0)
    tuple_1 = tuple_b + (0, 0)
    tuple_2 = (tuple_0[0] + tuple_1[0], tuple_0[1] + tuple_1[1])
    return tuple_2
