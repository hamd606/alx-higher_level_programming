#!/usr/bin/python3
"""this is a module that prints the last and firdt name"""

def say_my_name(first_name, last_name=""):
    """this function prints its valid input (names)"""
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
