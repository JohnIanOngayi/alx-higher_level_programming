#!/usr/bin/python3

def max_integer(my_list=[]):
    length = len(my_list)
    max = 0
    if length == 0:
        max = None
    else:
        for i in my_list:
            if i > max:
                max = i

    return max
