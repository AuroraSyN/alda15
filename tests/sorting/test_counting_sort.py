#!/usr/bin/env python
#-*- coding:utf-8 -*-


from algorithms_in_python.sorting import counting_sort

A = [2, 5, 3, 0, 2, 3, 0, 3]
R = [0, 0, 2, 2, 3, 3, 3, 5]


def test_heap_sort():
    assert R == counting_sort.sort(A, 5)
