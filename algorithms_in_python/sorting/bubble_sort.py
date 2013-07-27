#!/use/bin/env python
# -*- coding: utf-8 -*-

# Bubble Sort


def sort(array):
    for i in xrange(len(array) - 1):
        for j in xrange(len(array) - 1, i, -1):
            if array[j] < array[j - 1]:
                array[j - 1], array[j] = array[j], array[j - 1]
    return array
