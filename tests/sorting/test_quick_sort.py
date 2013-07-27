#!/usr/bin/env python
# -*- coding: utf-8 -*-

import data
from algorithms_in_python.sorting import quick_sort


def test_quick_sort():
    a_result = quick_sort.sort(data.array, 0, len(data.array) - 1)
    b_result = quick_sort.sort(data.brray, 0, len(data.brray) - 1)
    assert a_result == data.sorted_array
    assert b_result == data.sorted_brray
