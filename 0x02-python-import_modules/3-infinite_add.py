#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    _sum = 0

    for i in range(len(sys.argv) - 1):
        _sum += int(sys.argv[i + 1])

    print(f"{_sum}")
