#!/usr/bin/python3
import json
"""
    module:
        function that returns an object (Python data
        structure) represented by a JSON string
"""


def from_json_string(my_str):
    """
        args:
            my_str: object to be represented by a JSON string
        return:
            The object as represented by JSON string
    """
    return json.loads(my_str)
