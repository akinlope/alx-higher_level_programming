#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    myArr = matrix.copy()
    myLen = range(len(myArr))

    for i in myLen:
        myArr[i] = list(map(lambda x: x * x, myArr[i]))
    return(myArr)
