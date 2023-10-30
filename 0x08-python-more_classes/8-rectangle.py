#!/usr/bin/python3

"""
an empty class Rectangle that defines a rectangle
"""


class Rectangle:
    """
    a class Rectangle that defines a rectangle by dimensions
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        initialisation...

        args:
            width - width
            height - height
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        make width private
        args: none

        Returns: private width
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        sets width

        args:
            value - value

        Returns: none
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        make height private
        args: none

        Returns: private height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        sets height

        args:
            value - value

        Returns: none
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """area of rectangle

        args: none
        Returns: area
        """

        return (self.__width * self.__height)

    def perimeter(self):
        """perimeter of rectangle

        args: none
        Returns: perimeter
        """

        if (self.__width == 0 or self.__height == 0):
            perimeter = 0
        else:
            perimeter = 2 * (self.__width + self.__height)

        return (perimeter)

    def __str__(self) -> str:
        """
        returns printable rectangle with the character #
        """

        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                try:
                    rectangle += str(self.print_symbol)
                except Exception:
                    rectangle += type(self).print_symbol
            if column < self.__height - 1:
                rectangle += "\n"
        return (rectangle)

    def __repr__(self):
        """
        return a string representation of the rectangle
        to be able to recreate a new instance by using eval()

        args:none
        """

        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """prints a message for every object that is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
