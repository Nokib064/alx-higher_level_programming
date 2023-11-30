#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    i = 0
    for a in str:
        if i != n:
            new_str += a
        i += 1
    return new_str
