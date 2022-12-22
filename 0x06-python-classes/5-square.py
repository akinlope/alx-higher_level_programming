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
    
    @property
    def size(self):
        """ to retrive the property"""
        return self.__size
    
    @size.setter
    def size(self, value):
        """ a size setter """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        if (self.size <= 0):
            print(" ")
        else:
            for i in range(self.size):
                for x in range(self.size):
                    print("#", end="")
                print(" ")

