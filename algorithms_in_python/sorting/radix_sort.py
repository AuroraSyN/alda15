#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Radix Sort


def sort(array, d):
    for i in xrange(d - 1, -1, -1):
        insertion_sort(array, i)
    return array


def insertion_sort(array, d):
    for i in xrange(len(array)):
        key = array[i]
        j = i - 1
        while key[d] < array[j][d] and j >= 0:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array
