#!/usr/bin/python3

"""
class Rectangle that inherits from Base
"""

from models.base import Base


class Rectangle(Base):
    """
    class Rectangle that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialisation

        args:
            width - ...
            height - ...
            x - ...
            y - ...
            id - ...
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        elif value <= 0:
            raise ValueError("width must be > 0")
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
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
        make x private
        args: none

        Returns: private x
        """

        return self.__x

    @x.setter
    def x(self, value):
        """
        sets x

        args:
            value - value

        Returns: none
        """

        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """
        make y private
        args: none

        Returns: private y
        """

        return self.__y

    @y.setter
    def y(self, value):
        """
        sets y

        args:
            value - value

        Returns: none
        """

        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
            returns the area of the Rectangle instance.
        """

        return (self.__width * self.__height)

    def display(self):
        """
            prints to stdout the Rectangle instance with '#'
        """
        rectangle = ""
        print_symbol = "#"

#        for i in range(self.__height - 1):
#            rectangle += print_symbol * self.__width + "\n"
#        rectangle += print_symbol * self.__width

#        print("{}".format(rectangle))

        print("\n" * self.y, end="")

        for i in range(self.height):
            rectangle += (" " * self.x) + (print_symbol*self.width) + "\n"
        print(rectangle, end="")

    def __str__(self):
        """
            returns a string formart of the rectangle
        """
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                                self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
            assigns key/value argument to attributes
            kwargs is skipped if args is not empty
            Args:
                *args -  variable number of no-keyword args
                **kwargs - variable number of keyworded args
        """
        argc = len(args)
        kwargc = len(kwargs)
        modif_attrs = ['id', 'width', 'height', 'x', 'y']

        if argc > 5:
            argc = 5

        if argc > 0:
            for i in range(argc):
                setattr(self, modif_attrs[i], args[i])
        elif kwargc > 0:
            for k, v in kwargs.items():
                if k in modif_attrs:
                    setattr(self, k, v)

    def to_dictionary(self):
        """
        ...
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
