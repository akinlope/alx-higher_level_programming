#!/usr/bin/python3
"""a class Square"""


class Square:

    def __init__(self, size=0):
        """ a class Square
        create a new Instance of the Square
        Args:
            size (int): size of new Square
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif(size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
    
    def area(self):
        return self.__size * self.__size
    

    
