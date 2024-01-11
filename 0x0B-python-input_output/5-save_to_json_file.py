#!/usr/bin/python3
import json
"""
    module:
        function that writes an Object to a text
        file, using a JSON representation
"""


def save_to_json_file(my_obj, filename):
    """
        args:
            my_obj: object to be represented in JSON
            filename: file to be written
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
