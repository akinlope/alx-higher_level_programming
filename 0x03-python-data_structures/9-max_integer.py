#!/usr/bin/python3
def max_integer(my_list=[]):
    firstIndex = my_list[0]
    arrList = len(my_list) - 1
    # print(arrList)
    if arrList == 0:
        return(None)
    else:
        for i in my_list:
            if i > firstIndex:
                firstIndex = i
        return(firstIndex)
