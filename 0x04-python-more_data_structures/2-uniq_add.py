#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_newlist = set()
    for index in my_list:
        my_newlist.add(index)
    temp = sum(my_newlist)
    return temp
