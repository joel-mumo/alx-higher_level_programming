#!/usr/bin/python3
"""This defines a class square"""


class Square:
    """Initialises a new square
    Args:
        size (int): The size of the new square
    """
    def __init__(self, size=0):
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Returnss the area of a square"""
        return self.__size ** 2
