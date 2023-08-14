#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    output = []
    for i in my_list:
        if i % 2 == 0:
            #print("{:d} is divisible by 2".format(i))
            output.append(True)

        else:
            #print("{:d} is not divisible by 2".format(i))
            output.append(False)

    return output
