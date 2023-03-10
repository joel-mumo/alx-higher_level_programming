#!/usr/bin/python3
"""Define a class Square.
This module contains a class that defines a square and
its size and checking if the given values are right
"""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialises a new square.
        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Define the == comparison to a Square.
        Args:
            other (Square): the square object to compare with.
        """
        if type(other) is Square:
            return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a Square.
        Args:
            other (Square): the Square object to compare with.
        """
        if type(other) is Square:
            return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to a Square.
        Args:
            other (Square): the Square object to compare with.
        """
        if type(other) is Square:
            return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a Square.
        Args:
            other (Square): the Square object to compare with.
        """
        if type(other) is Square:
            return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a Square.
        Args:
            other (Square): the Square object to compare with.
        """
        if type(other) is Square:
            return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= compmarison to a Square.
        Args:
            other (Square): the Square object to compare with.
        """
        if type(other) is Square:
            return self.area() >= other.area()
