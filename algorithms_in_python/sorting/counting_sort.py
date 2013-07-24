#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Counting Sort


def sort(array, max_num):
    num_list = [0 for i in range(max_num + 1)]
    output_list = [0 for i in range(len(array))]

    for i in range(len(array)):
        num_list[array[i]] += 1
    # num_list[i] now contains elements equals to i.

    for i in range(1, max_num + 1):
       num_list[i] += num_list[i - 1]
    # num_list[i] now contains elements less than or equals to i.

    for i in range(len(array) - 1, -1, -1):
        print num_list[array[i]]
        output_list[num_list[array[i]] - 1] = array[i]
        num_list[array[i]] -= 1
    return output_list
