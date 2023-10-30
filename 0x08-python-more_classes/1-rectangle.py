#!/usr/bin/python3

"""
an empty class Rectangle that defines a rectangle
"""


class Rectangle:
    """
    a class Rectangle that defines a rectangle by dimensions
    """

    def __init__(self, width=0, height=0):
        """
        initialisation...

        args:
            width - width
            height - height
        """

        self.width = width
        self.height = height

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
