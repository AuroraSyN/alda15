#!/usr/bin/env python
# -*- coding: utf-8 -*-


import data
from algorithms_in_python.sorting import shell_sort


def test_shell_sort():
    a_result = shell_sort.sort(data.array)
    b_result = shell_sort.sort(data.brray)
    assert a_result == data.sorted_array
    assert b_result == data.sorted_brray
 
