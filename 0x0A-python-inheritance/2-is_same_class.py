#!/usr/bin/python3
""" module:
        function that returns True if the object is exactly
        an instance of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """
        Returns:
            True if the object is exactly an instance
            of the specified class ; otherwise False
        args:
            obj: object to check its class
            a_class: specified class to check
    """
    if type(obj) is not a_class:
        return False
    else:
        return True
