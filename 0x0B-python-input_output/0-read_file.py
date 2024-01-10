#!/usr/bin/python3
"""
    module:
        function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    args:
        filename: file to be read
    """
    with open(filename, "r", encoding="utf8") as f:
        print(f.read())
