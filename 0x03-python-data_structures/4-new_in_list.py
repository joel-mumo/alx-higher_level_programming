#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list_len = len(my_list)
    n_copy = my_list.copy()
    if idx < 0 or idx > my_list_len - 1:
        return n_copy
    else:
        n_copy[idx] = element
        return n_copy
