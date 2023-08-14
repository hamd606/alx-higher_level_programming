#!/usr/bin/python3
def no_c(my_string):
    my_copy = [x for x in my_string if x != 'c' and x != 'C']
    result = "".join(my_copy)
    return (result)
