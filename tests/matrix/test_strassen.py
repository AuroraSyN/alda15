#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Test Strassen


import random
from algorithms_in_python.matrix import strassen


A = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]

B = [[5, 3, 0, 6],
     [1, 5, 6, 8],
     [2, 7, 4, 9],
     [7, 3, 8, 2]]

R = [[41, 46, 56, 57],
     [101, 118, 128, 157],
     [161, 190, 200, 257],
     [221, 262, 272, 357]]


def test_primitive_mul():
    assert R == strassen.primitive_mul(A, B)


def test_strassen():
    # n <= leaf_size, using primitive multiplication
    assert R == strassen.strassen(A, B)
    # n > leaf_size, using strassen's algorithm
    C = strassen.init_matrix(128, random.randint(0, 100))
    D = strassen.init_matrix(128, random.randint(0, 100))
    PR = strassen.primitive_mul(C, D)
    SR = strassen.strassen(C, D)
    assert PR == SR
