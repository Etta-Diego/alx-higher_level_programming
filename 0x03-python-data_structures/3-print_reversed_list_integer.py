#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return None
    copy = my_list
    for ind in copy[::-1]:
        print("{:d}".format(ind))
