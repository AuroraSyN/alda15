#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Bucket Sort


import math


def sort(array):
    n = len(array)
    bucket = [[] for i in xrange(n)]
    output = []
    for i in xrange(n):
        bucket[int(math.floor(n * array[i]))].append(array[i])
    for i in xrange(n):
        bucket[i] = insertion_sort(bucket[i])
    for i in xrange(n):
        output +=  bucket[i]
    return output


def insertion_sort(array):
    for i in xrange(len(array)):
        key = array[i]
        j = i - 1
        while key < array[j] and j >= 0:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array
