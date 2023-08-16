#!/usr/bin/python3
def search_replace(my_list, search, replace):
    tmp_list = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            tmp_list.append(replace)
        else:
            tmp_list.append(my_list[i])
    return tmp_list
