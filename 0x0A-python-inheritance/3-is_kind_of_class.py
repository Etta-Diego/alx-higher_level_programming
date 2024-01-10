#!/usr/bin/python3
"""
    module:
        This function takes two arguments: the object and the
        class and returns True if the object is an instance
        of, or if the object is an instance of a class that
        inherited from, the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
        args:
            object: the instance of the class
            a_class: the specified class
        Returns:
            True if the object is an instance of, or if
            the object is an instance of a class that inherited
            from, the specified class ; otherwise False.
    """
    return isinstance(obj, a_class)
