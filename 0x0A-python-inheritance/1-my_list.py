#!/usr/bin/python3
""" Class that inherits the attributes references of class list """


class MyList(list):
    """ Class that inherits the attributes references of class list
    Args:
        list: class list
    """

    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
