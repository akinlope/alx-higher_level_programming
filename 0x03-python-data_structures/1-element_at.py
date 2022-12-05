#!/usr/bin/python3
def element_at(my_list, idx):
    myLen = len(my_list)
    if (idx < 0):
        return (None)
    elif (idx > myLen):
        return (None)
    else:
        return (my_list[idx])
