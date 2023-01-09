#!/usr/bin/python3
def no_c(my_string):
    n_copy = my_string.translate({ord(i): None for i in 'cC'})
    return n_copy
