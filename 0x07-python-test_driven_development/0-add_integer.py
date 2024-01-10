#!/usr/bin/python3
""" module:
    function that accepts and add two integers 
"""


def add_integer(a, b=98):
    """ Returns the sum of two integers
        args:
            a: must be integer or float
            b: must be integer or float
        
        raise:
            TypeError: must be an integer
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
