#!/usr/bin/python3

"""Defines a function for appending files"""


def append_write(filename="", text=""):
    """Appends a string to a text(UTF8) file
    Args:
        filename: The file to be appended to
        text: The string to be appended to filename
    Returns:
        The number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
