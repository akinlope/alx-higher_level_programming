def divisible_by_2(my_list=[]):
    newList = []
    # print(my_list)
    # print(newList)
    for i in my_list:
        if i % 2 == 0:
            newList.append(True)
        else:
            newList.append(False)
    return(newList)
