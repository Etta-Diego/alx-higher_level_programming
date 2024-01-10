#!/usr/bin/python3
def no_c(my_string):
    str1 = ""
    for char in my_string:
        if char != "c" and char != "C":
            str1 += char
    return str1
