#!/usr/bin/python3
"""

This module contains a function that prints a text with 2 new lines after
the characters `.`, `?` and `:`

"""


def text_indentation(text):
    """

    Prints text definitively when certain characters are encountered

    Args:
    text (str): the string to be printed

    Raises:
    TypeError: when text is not a string

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_str = text.split()
    new_str = " ".join(new_str)
    new_str = new_str.replace(".", ".\n\n")
    new_str = new_str.replace(":", ":\n\n")
    new_str = new_str.replace("?", "?\n\n")
    new_str = new_str.replace("\n ", "\n")

    print(new_str, end='')
