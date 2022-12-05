#!/usr/bin/python3
def no_c(my_string):
    empty = ""
    for i in my_string:
        if (i[0] != "c") and (i[0] != "C"):
            empty += i[0]
    return(empty)
