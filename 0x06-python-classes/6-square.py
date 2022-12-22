#!/usr/bin/python3
"""a class Square"""


class Square:

    def __init__(self, size=0, position=(0, 0)):
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
        self.__position = position

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

    @property
    def position(self):
        """to retrieve the property"""
        return self.__position

    @position.setter
    def position(self, value):
        myLen = len(value)
        if(myLen < 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif(value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
