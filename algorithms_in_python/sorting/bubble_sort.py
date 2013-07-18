#!/use/bin/env python
#-*- coding:utf-8 -*-

# Bubble Sort


def sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1, i, -1):
            if array[j] < array[j - 1]:
                temp = array[j - 1]
                array[j - 1] = array[j]
                array[j] = temp
    return array
