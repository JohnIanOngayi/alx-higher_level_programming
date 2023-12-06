#!/usr/bin/python3

def complex_delete(a_dictionary, value):

    delete = []
    if value in a_dictionary.values():
        _delete = [key for key, val in a_dictionary.items() if val == value]

        for key in _delete:
            del a_dictionary[key]

    return a_dictionary
