#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """This represents a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialises a square
        Args:
            size (int): The size of the new square
            position (int, int): The position of the new square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Set the size of the square"""
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

    @property
    def position(self):
        """Set the position of the square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square with the # character on stdout."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
