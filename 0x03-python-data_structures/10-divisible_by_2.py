#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    length = len(my_list)
    relip = list(())
    for i in range(0, length):
        if my_list[i] % 2 == 0:
            relip.append(True)
        else:
            relip.append(False)
    return relip
