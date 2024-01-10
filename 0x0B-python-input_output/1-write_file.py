#!/usr/bin/python3
"""
    module:
         function that writes a string to a text file
         (UTF8) and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    args:
        filename: text file to write to.
        text: text to be written
    Returns:
        length of the text written
    """
    with open(filename, "w", encoding="utf8") as f:
        f.write(text)
        return len(text)
