#!/usr/bin/env python
# -*- coding: utf-8 -*-


from algorithms_in_python.string import max_subarray


array = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]


def test_max_subarray():
    low, high, sum = max_subarray.find_max_subarray(array, 0, len(array) - 1)
    assert low == 7
    assert high == 10
    assert sum == 43
