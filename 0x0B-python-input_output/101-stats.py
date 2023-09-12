#!/usr/bin/python3
"""prints stats from stdin according to task"""


import sys
import io

size = 0
dictionary_status = {}
count = 0
for line in sys.stdin:
    split = line.split()
    status = split[-2]
    size += int(split[-1])
    if status in dictionary_status.keys():
        dictionary_status[status] += 1
    else:
        dictionary_status[status] = 1
    count += 1
    if count == 10:
        sortme = sorted(dictionary_status.keys())
        print("File size:", size)
        for keys in sortme:
            print("{}: {}".format(keys, dictionary_status[keys]))
        count = 0
        continue
