#!/usr/bin/python3

"""Define a class Student"""


class Student:
    """This represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initialises a new student
        Args:
            first_name: first name of student
            last_name: last name of student
            age: age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets a Dict representation of a student"""

        my_dict = dict()
        if type(attrs) is list and all(type(x) is str for x in attrs):
            for x in attrs:
                if x in self.__dict__:
                    my_dict.update({x: self.__dict__[x]})
            return my_dict
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for x, v in json.items():
            setattr(self, x, v)
