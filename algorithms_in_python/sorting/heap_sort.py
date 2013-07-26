#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Heap Sort


parent = lambda i: (i - 1) / 2
left = lambda i: 2 * i + 1
right = lambda i: 2 * (i + 1)


def max_heapify(array, i):
    """ maintain the property of max-heap"""
    l = left(i)
    r = right(i)
    if l < len(array) and array[l] > array[i]:
        largest = l
    else:
        largest = i
    if r < len(array) and array[r] > array[largest]:
        largest = r
    if largest is not i:
        array[i], array[largest] = array[largest], array[i]
        max_heapify(array, largest)
    return array


def build_max_heap(array):
    """ build a max-heap."""
    for i in reversed(xrange(len(array) / 2)):
        max_heapify(array, i)
    return array


def sort(array):
    """ implement the heap sort algorithm."""
    build_max_heap(array)
    for i in xrange(len(array) - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        array[:i-len(array)] = max_heapify(array[:i-len(array)], 0)
    return array
