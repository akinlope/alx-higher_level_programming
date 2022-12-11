#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    res = sorted(a_dictionary)
    for i in res:
        print(f"{i}: {a_dictionary[i]}")
