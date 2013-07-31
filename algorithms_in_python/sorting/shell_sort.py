#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Shell Sort


def sort(array):
    # using Marcin Ciura's gap sequence
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]
    for gap in gaps:
        for i in range(gap, len(array)):
            tmp = array[i]
            j = i
            while j >= gap and tmp < array[j - gap]:
                array[j] = array[j - gap]
                j -= gap
            array[j] = tmp
    return array
