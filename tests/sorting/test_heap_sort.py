#!/usr/bin/env python
#-*- coding:utf-8 -*-


import data
from algorithms_in_python.sorting import heap_sort


def test_heap_sort():
    a_result = heap_sort.sort(data.array)
    b_result = heap_sort.sort(data.brray)
    assert data.sorted_array == a_result
    assert data.sorted_brray == b_result
