#!/usr/bin/env python
#-*- encoding:utf-8 -*-


from algorithms_in_python.sorting import radix_sort


A = ['COW', 'DOG', 'SEA', 'RUG', 'ROW', 'MOB', 'BOX', 'TAB', 'BAR', 'EAR',
     'TAR', 'DIG', 'BIG', 'TEA', 'NOW', 'FOX']
R = ['BAR', 'BIG', 'BOX', 'COW', 'DIG', 'DOG', 'EAR', 'FOX', 'MOB', 'NOW',
     'ROW', 'RUG', 'SEA', 'TAB', 'TAR', 'TEA']


def test_radix_sort():
    assert R == radix_sort.sort(A, 3)
