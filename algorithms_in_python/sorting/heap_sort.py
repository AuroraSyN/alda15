#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Heap Sort


def parent(i):
    """ return parent node's index in the array."""
    return (i - 1) / 2


def left(i):
    """ return left child node's index in the array."""
    return 2 * i + 1


def right(i):
    """ return right child node's index in the array."""
    return 2 * (i + 1)


def max_heapify(array, i):
    """ maintain the property of max-heap"""
    l = left(i)
    r = right(i)
    heap_size = len(array)
    if l < heap_size and array[l] > array[i]:
        largest = l
    else:
        largest = i
    if r < heap_size and array[r] > array[largest]:
        largest = r
    if largest is not i:
        tmp = array[i]
        array[i] = array[largest]
        array[largest] = tmp
        max_heapify(array, largest)
    return array


def build_max_heap(array):
    """ build a max-heap."""
    for i in xrange(len(array) / 2 - 1, -1, -1):
        max_heapify(array, i)
    return array


def sort(array):
    """ implement the heap sort algorithm."""
    build_max_heap(array)
    for i in xrange(len(array) - 1, 0, -1):
        tmp = array[0]
        array[0] = array[i]
        array[i] = tmp
        array[:i-len(array)] = max_heapify(array[:i-len(array)], 0)
    return array
