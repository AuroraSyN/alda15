#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Insertion Sort

import util


def insertion_sort(array, ascend=True):
    for i in range(len(array)):
        key = array[i]
        j = i - 1
        if ascend is True:
            while key < array[j] and j >= 0:
                array[j+1] = array[j]
                j -= 1
        else:
            while key > array[j] and j >= 0:
                array[j+1] = array[j]
                j -= 1
        array[j+1] = key
    return array


if __name__ == "__main__":
    l = util.generate_array(15)
    print l
    array = insertion_sort(l, False)
    print array
