#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    rd = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ian = 0
    for i in range(len(roman_string)):
        if i > 0 and rd[roman_string[i]] > rd[roman_string[i - 1]]:
            ian += rd[roman_string[i]] - 2 * rd[roman_string[i - 1]]
        else:
            ian += rd[roman_string[i]]
    return ian
