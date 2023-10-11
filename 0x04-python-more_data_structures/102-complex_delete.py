#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    delete_list = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            delete_list.append(key)
    for key in delete_list:
        del a_dictionary[key]
    return a_dictionary
