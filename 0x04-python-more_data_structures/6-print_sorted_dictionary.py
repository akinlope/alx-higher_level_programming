#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    res = sorted(a_dictionary.items(), key=lambda x: x[0])
    print(dict(res))
