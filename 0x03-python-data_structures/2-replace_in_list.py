#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    length = len(my_list)
    if idx < 0 or idx >= length:
        return my_list
    for ind in range(length):
        if 0 <= idx < length:
            my_list[idx] = element
    return my_list
