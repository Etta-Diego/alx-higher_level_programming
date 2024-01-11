#!/usr/bin/python3
"""
    module:
        function that appends a string at the end of a text
        file (UTF8) and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    args:
        filename: file to be read
        text: text to written in the file
    Return:
        number of characters added.
    """
    with open(filename, "a", encoding="utf8") as f:
        f.write(text)
        return len(text)
