#!/usr/bin/python3
def madic_string():
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return ("BestSchool, " * (magic_string.n -1) + "BestSchool")
