#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Quick Sort


def sort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        sort(array, p, q - 1)
        sort(array, q + 1, r)
    return array


def partition(array, p, r):
    x = array[r]
    i = p - 1
    for j in xrange(p, r):
        if array[j] <= x:
            i += 1
            tmp = array[i]
            array[i] = array[j]
            array[j] = tmp
    tmp = array[i + 1]
    array[i + 1] = array[r]
    array[r] = tmp
    return i + 1
