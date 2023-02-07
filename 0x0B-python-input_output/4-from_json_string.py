#!/usr/bin/python3

"""Defines an object(string) to JSON function"""
import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string"""
    return json.loads(my_str)
