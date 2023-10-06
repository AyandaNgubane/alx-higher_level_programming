#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if (len(tuple_a) == 0):
        t_tuple = (0, 0)
        tuple_a = t_tuple
    elif (len(tuple_a) == 1):
        t_tuple = ((tuple_a[0]), 0)
        tuple_a = t_tuple

    if (len(tuple_b) == 0):
        t_tuple = (0, 0)
        tuple_b = t_tuple
    elif (len(tuple_b) == 1):
        t_tuple = ((tuple_b[0]), 0)
        tuple_b = t_tuple

    my_tuple = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))

    return my_tuple
