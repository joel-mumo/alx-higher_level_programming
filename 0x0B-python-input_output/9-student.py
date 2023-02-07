#!/usr/bin/python3

"""Define a cladd student"""


class Student:
    """This represents a student"""

    def __init__(self, first_name, last_name, age):
        """This initialises a new student
        Args:
            first_name: first name of the student
            last_name: last name the student
            age: age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Define a dict representation of the student"""
        return self.
