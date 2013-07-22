#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Strassen


def init_matrix(size, value=0):
    """ generate a matrix of given size and set all element to given value,
        default 0.
    """
    return [[value for i in xrange(size)] for j in xrange(size)]


def add(mat1, mat2):
    n = len(mat1)
    new_mat = init_matrix(n)
    for i in xrange(n):
        for j in xrange(n):
            new_mat[i][j] = mat1[i][j] + mat2[i][j]
    return new_mat


def sub(mat1, mat2):
    n = len(mat1)
    new_mat = init_matrix(n)
    for i in xrange(n):
        for j in xrange(n):
            new_mat[i][j] = mat1[i][j] - mat2[i][j]
    return new_mat


def primitive_mul(mat1, mat2):
    """ the original O(n^3) matrix multiplication. """
    n = len(mat1)
    new_mat = init_matrix(n)
    for i in xrange(n):
        for j in xrange(n):
            for k in xrange(n):
                new_mat[i][j] += mat1[i][k] * mat2[k][j]
    return new_mat


def strassen(mat1, mat2, leaf_size=16):
    """ strassen's matrix multiplication algorithm."""
    n = len(mat1)
    if n <= leaf_size:
        return primitive_mul(mat1, mat2)
    else:
        size = n / 2
        # initialize sub-matrices
        a11, a12, a21, a22, b11, b12, b21, b22 = [
            init_matrix(size) for i in range(8)]
        # divide matrix into 4 sub-matrices
        for i in xrange(size):
            for j in xrange(size):
                a11[i][j] = mat1[i][j]                # top-left
                a12[i][j] = mat1[i][j + size]         # top-right
                a21[i][j] = mat1[i + size][j]         # bottom-left
                a22[i][j] = mat1[i + size][j + size]  # bottom-right

                b11[i][j] = mat2[i][j]
                b12[i][j] = mat2[i][j + size]
                b21[i][j] = mat2[i + size][j]
                b22[i][j] = mat2[i + size][j + size]

        # calculate p1 to p7
        p1 = strassen(add(a11, a22), add(b11, b22))   # p1 = (a11+a22)(b11+b22)
        p2 = strassen(add(a21, a22), b11)             # p2 = (a21+a22)a11
        p3 = strassen(a11, sub(b12, b22))             # p3 = a11(b12-b22)
        p4 = strassen(a22, sub(b21, b11))             # p4 = a22(b21-b11)
        p5 = strassen(add(a11, a12), b22)             # p5 = (a11+a12)b22
        p6 = strassen(sub(a21, a11), add(b11, b12))   # p6 = (a21-a11)(b11+b12)
        p7 = strassen(sub(a12, a22), add(b21, b22))   # p7 = (a12-a22)(b21+b22)

        # calculate c11, c12, c21, c22
        c11 = add(sub(add(p1, p4), p5), p7)           # c11 = p1 + p4 - p5 + p7
        c12 = add(p3, p5)                             # c12 = p3 + p5
        c21 = add(p2, p4)                             # c21 = p2 + p4
        c22 = add(add(sub(p1, p2), p3), p6)           # c22 = p1 - p2 + p3 + p6

        # combine 4 parts into a single matrix
        mat_c = init_matrix(n)
        for i in xrange(size):
            for j in xrange(size):
                mat_c[i][j] = c11[i][j]
                mat_c[i][j + size] = c12[i][j]
                mat_c[i + size][j] = c21[i][j]
                mat_c[i+size][j + size] = c22[i][j]
        return mat_c
