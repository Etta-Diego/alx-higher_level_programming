#!/usr/bin/python3
import json
"""
    module:
        function that returns the JSON representation
        of an object (string)
"""


def to_json_string(my_obj):
    """
        args:
            my_obj: object to be represented in JSON
        return:
            the JSON representation of the object
    """
    return json.dumps(my_obj)
