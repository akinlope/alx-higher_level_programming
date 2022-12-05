#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    ownList = my_list.copy()
    ownList.reverse()
    for i in ownList:
        print("{}".format(i))
