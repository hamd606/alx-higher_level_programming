#!/usr/bin/python3

def print_last_digit(number):
    
    number = abs(number)
    digit = number % 10

    print(f"{digit:d}", end="")

    return digit
