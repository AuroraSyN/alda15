#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Counting Sort


def sort(array, max_num):
    num_list = [0 for i in xrange(max_num + 1)]
    output_list = [0 for i in array]

    for item in array:
        num_list[item] += 1
    # num_list[i] now contains elements equals to i.

    for i in xrange(1, max_num + 1):
        num_list[i] += num_list[i - 1]
    # num_list[i] now contains elements less than or equals to i.

    for item in reversed(array):
        output_list[num_list[item] - 1] = item
        num_list[item] -= 1
    return output_list
