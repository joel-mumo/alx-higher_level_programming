#!/usr/bin/python3

"""Define a class students"""


class Student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initialises a new students
        Args:
            first_name: first name of the student
            last_name: last name of the student
            age: age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets a dictionary representation of a Student instance"""
        return {s: v for s, v in self.__dict__.items() if s in attrs}
    return self.__dict__
