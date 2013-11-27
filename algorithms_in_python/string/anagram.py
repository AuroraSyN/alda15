#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import itertools


def group(word_list):
    d = defaultdict(list)
    for l in word_list:
        sorted_l = ''.join(sorted(l))
        d[sorted_l] += [l]
    for key in d:
        print d[key]


def permutation(word_list):
    return ["".join(p) for p in itertools.permutations(word_list)]

def all_perms(elements):
    if len(elements) <=1:
        return elements
    else:
        tmp = []
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                tmp.append(perm[:i] + elements[0:1] + perm[i:])
        return tmp
