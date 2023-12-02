#!/usr/bin/python3
"""finds max of a list"""


def find_peak(list_of_integers):
    """finds the max of a list"""

    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
    else:
        return None
