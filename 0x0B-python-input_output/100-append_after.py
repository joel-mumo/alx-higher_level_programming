#!/usr/bin/python3

"""Defines a function that inserts a text file"""


def append_after(filename="", search_string="", new_string=""):
    """Insets text after each line containing a given string in a file
    Args:
        filename: name of file
        search_string:string to search for within the file
        new_string: string to insert
    """

    text = ""
    with open(filename, 'r') as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, 'w') as f:
        f.write(text)
