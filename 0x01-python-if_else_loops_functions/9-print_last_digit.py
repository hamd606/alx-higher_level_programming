#!/usr/bin/python3

def print_last_digit(number):

    if number == 0:
        print(f"0"; end="")
        return 0

    number = abs(number)
    digit = number % 10

    print(f"{digit:d}", end="")

    return digit
