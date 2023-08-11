#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":

    argc = len(argv) - 1
    if argc != 3:
        print("Usage: {:s} <a> <operator> <b>".format(argv[0]))
        exit(1)
    elif argv[2] == '+':
        func = add
    elif argv[2] == '-':
        func = sub
    elif argv[2] == '*':
        func = mul
    elif argv[2] == '/':
        func = div
    else:
        print(("Unknown operator. Available operators: +, -, *, and /"))
        exit(1)

    result = func(int(argv[1]), int(argv[3]))
    x = int(argv[1])
    y = argv[2]
    z = int(argv[3])
    print("{:d} {:s} {:d} = {:d}".format(x, y, z, result))
