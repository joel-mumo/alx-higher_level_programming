#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """This represents a square"""
    def __init__(self, size=0):
        """Initialises a new square
        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Sets the size of a square"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2
