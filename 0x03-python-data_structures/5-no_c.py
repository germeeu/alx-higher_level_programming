#!/usr/bin/env python3
def no_c(my_string):
    new_string = [n for n in my_string if n != 'C' or n != 'c']
    return("".join(new_string))
