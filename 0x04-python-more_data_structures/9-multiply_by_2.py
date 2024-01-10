#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    if a_dictionary is None:
        return None
    for value in a_dictionary:
        new_dict[value] = a_dictionary[value] * 2
    return new_dict
#        print("{}: {:d}".format(value, new_dict[value]))
