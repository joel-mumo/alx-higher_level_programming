#!/usr/bin/python3

"""Defines an inherited list class MyList."""


class MyList(list):
    """Defines the MyList class."""
    def print_sorted(self):
        """Prints the sorted list."""
        print(sorted(self))
