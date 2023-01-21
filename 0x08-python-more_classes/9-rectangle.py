#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle by: (based on 8-rectangle.py)
"""


class Rectangle:
    """
    Class that defines a rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        the intialising stage for our Class model
        args:
        Width: determines the width of our Rectangle
        Height: determines the height of our Rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        A property getter that gets the the width of our Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter Method used to reasign the private variable width
        args:
        Value: the new width we are setting
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """
        A property getter that gets the the height of our Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter Method used to reasign the private variable height
        Args:
        Value- the new height we are setting
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        """
        Calculate the area of our rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of our rectangle
        """
        perim = 2 * (self.__width + self.__height)

        if self.__width == 0 or self.__height == 0:
            perim = 0
        return perim

    def __str__(self) -> str:
        """
        Method returning the string value represented with #
        if width or height is 0 an empty string is retuned
        """
        rect = ""

        if self.__width == 0 or self.__height == 0:
            return rect

        for i in range(self.height):
            rect += (str(self.print_symbol) * self.width) + "\n"

        return rect[:-1]

    def __repr__(self) -> str:
        """ Method will return a string representation of
        the rectangle to be able to recreate a new instance
        by using eval()
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Method that delete an instance and shows a message afterward
        it also reduces the number of instance!
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Static method that returns the biggest
        rectangle based on the area
        Args:
            rect_1: instance 1 of Rectangle class
            rect_2: instance 2 of Rectangle class
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        class method that returns rectangle instance
        in a square shape
        Args:
            cls: A new Class instance
            Size: our new given size
        Return:
            A square shape i.e equal size
        """
        return cls(size, size)
