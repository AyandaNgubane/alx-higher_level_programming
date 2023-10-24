#!/usr/bin/python3

"""class Square that defines a square"""


class Square:
    """class Square that defines a square"""

    def __init__(self, size=0):
        """attributes

        args:
            size - size of square
            """

        self.size = size

    @property

    def size(self):
        """make size private

        args: none

        Return: private size
        """

        return self.__size

    @size.setter

    def size(self, value):
        """sets size

        args:
            value - value
        Return: none
        """

        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """area of square

        args: none
        Returns: area
        """

        return (self.__size ** 2)
