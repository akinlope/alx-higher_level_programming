#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    myLen = len(my_list) - 1
    if idx < 0 or idx > myLen:
        return new_list
    else:
        new_list[idx] = element
        return new_list
