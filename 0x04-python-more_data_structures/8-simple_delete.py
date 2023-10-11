#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    new_dict = a_dictionary.copy()
    for o_key in new_dict:
        if o_key == key:
            del a_dictionary[key]
    return a_dictionary
