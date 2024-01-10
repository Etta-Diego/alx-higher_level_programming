#!/usr/bin/python3
"""
class:
    A class that inherits from list
"""


class MyList(list):
    """
    module:
        method that calls the list constructor with the given arguments
    """
    def __init__(self, *args):
        list.__init__(self, *args)

    """
    module:
        public instance method that prints the list,
        but sorted (ascending sort)
    """
    def print_sorted(self):
        """
        args:
            elements to be sorted
        """
        print(sorted(self))
