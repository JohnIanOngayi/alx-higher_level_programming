#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):

    my_list.reverse()
    for i in range(0, len(my_list)):
        print("{0:d}".format(my_list[i]))
