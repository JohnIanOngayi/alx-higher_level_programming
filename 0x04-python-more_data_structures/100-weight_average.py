#!/usr/bin/python3

def weight_average(my_list=[]):

    sum_total = 0
    denominator = 0
    average = 0

    if len(my_list) != 0:

        for i in my_list:
            a, b = i
            denominator += b
            sum_total += a*b

        average = sum_total / denominator

    return average
