#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    [print("{}: {}".format(e, a_dictionary[e])) for e in sorted(a_dictionary)]
