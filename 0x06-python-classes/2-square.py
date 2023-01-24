#!/usr/bin/python3
"""This defines a class square and init method"""


class Square:
    """This defines a square"""
    def __init__(self, size=0):
        """Initialises a new square.
        Args:
            size (int): The size of the new square.
        """
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
