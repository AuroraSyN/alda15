#!/usr/bin/env python
#-*- coding:utf-8 -*-


from algorithms_in_python.sorting import heap_sort


A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
R = [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]

def test_heap_sort():
    assert R == heap_sort.sort(A) 
