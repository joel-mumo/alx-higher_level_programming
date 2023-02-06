#!/usr/bin/python3

"""Defines function that compares an object with an instance"""



def inherits_from(obj, a_class):
   """Checks if an object is an inherited instance of a class
   Args:
        obj (any): Object to check
        a_class (type): Class to match the type of obj to
    Returns:
        True if obj is an inherited instance of a_class
        Otherwise, false
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
