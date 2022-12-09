#!/usr/bin/python3

def uniq_add(my_list=[]):
    newList = []
    ans = 0

    for i in my_list:
        if i not in newList:
            newList.append(i)
    for n in newList:
        ans = ans + n
    return(ans)
