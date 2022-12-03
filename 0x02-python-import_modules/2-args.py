#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    lens = len(argv) - 1
    n = 1
    if (lens == 0):
        print("{} arguments.".format(lens))
    elif (lens == 1):
        print("{} argument:".format(lens))
        for n in range(lens):
            print("{}: {}".format(lens, argv[1]))
    else:
        print("{} arguments:".format(lens))
        for n in range(lens):
            n = n + 1
            print("{}: {}".format(n, argv[n]))
