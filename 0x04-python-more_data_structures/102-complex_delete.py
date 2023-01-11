#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for a, b in list(a_dictionary.items()):
        if b is value:
            a_dictionary.pop(a)
    return a_dictionary
