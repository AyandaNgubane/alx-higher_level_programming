#!/usr/bin/python3

"""
function that prints a text with 2 new lines after each of these characters: ., ? and :

Prototype: def text_indentation(text):
text must be a string, otherwise raise a TypeError exception with the message text must be a string
There should be no space at the beginning or at the end of each printed line
"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines after
    each of these characters: ., ? and :

    args:
        text - text

    Returns: nothing
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    j = 10000

    for i in text:
        if j == 10000:
            if i == " ":
                continue
        if i == "." or i == "?" or i == ":":
            print(i)
            print()
            j = 0
        else:
            if j == 0:
                i = ""
            print(i, end="")
            j =+ 1
