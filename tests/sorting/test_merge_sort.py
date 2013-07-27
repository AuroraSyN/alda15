#!/usr/bin/env python
# -*- coding: utf-8 -*-

import data
from algorithms_in_python.sorting import merge_sort


def test_merge_sort():
    a_result = merge_sort.sort(data.array, 0, len(data.array) - 1)
    b_result = merge_sort.sort(data.brray, 0, len(data.brray) - 1)
    assert a_result == data.sorted_array
    assert b_result == data.sorted_brray
