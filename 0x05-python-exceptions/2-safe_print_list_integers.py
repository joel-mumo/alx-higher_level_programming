#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    r = 0
    for i range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            r += 1
        except (TypeError, ValueError):
            continue
    print()
    return r
