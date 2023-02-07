#!/usr/bin/python3

"""Defines a fucntion for writing files"""


def write_file(filename="", text=""):
    """Write a string to a text (UTF8) file
    Args:
        filename: The name of the file to write
        text: text to be written to the file
    Returns:
        The number of chars written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
