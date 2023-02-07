#!/usr/bin/python3

"""This defines a function that reads text files"""


def read_file(filename=""):
    """Prints the contents of a text file (UTF8) to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
