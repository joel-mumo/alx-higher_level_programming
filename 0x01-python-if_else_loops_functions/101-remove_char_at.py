#!/usr/bin/python3
def remove_char_at(str, n):
    copys = ''
    i = 0
    for c in str:
        if i != n:
            copys += str[i]
        i += 1
    return copys
