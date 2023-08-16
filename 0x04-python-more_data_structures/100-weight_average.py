#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list == []:
        return 0
    weights_sum = 0
    scores_sum = 0

    for i in my_list:
        weights_sum += i[1]
        scores_sum += i[1] * i[0]

    return scores_sum / weights_sum
