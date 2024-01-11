#!/usr/bin/python3
import json
"""
    module:
        function that creates an Object from a “JSON file”
"""


def load_from_json_file(filename):
    """
        args:
            filename:
                JSON file
        return:
            the created object from the JSON file
    """
    with open(filename, "r") as f:
        return json.load(f)
