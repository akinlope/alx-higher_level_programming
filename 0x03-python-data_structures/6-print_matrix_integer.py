#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        my_length = len(i) - 1
        for n in i:
            if n != i[my_length]:
                print("{:d}".format(n), end=" ")
                # print("Helo wrold")
            if n == i[my_length]:
                print("{:d}".format(n), end="")
        print()
