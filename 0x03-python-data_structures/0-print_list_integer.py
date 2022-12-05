#!/usr/bin/python3
def print_list_integer(my_list=[]):
    getLen = len(my_list)
    for i in range(getLen):
        print("{:d}".format(my_list[i]))
        # print(type(my_list[i]))
