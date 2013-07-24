#!/usr/bin/env python
#-*- coding:utf-8 -*-


from algorithms_in_python.sorting import bucket_sort

A = [0.79, 0.13, 0.16, 0.64, 0.39, 0.20, 0.89, 0.53, 0.71, 0.42]
R = [0.13, 0.16, 0.20, 0.39, 0.42, 0.53, 0.64, 0.71, 0.79, 0.89]


def test_bucket_sort():
    assert R == bucket_sort.sort(A)
