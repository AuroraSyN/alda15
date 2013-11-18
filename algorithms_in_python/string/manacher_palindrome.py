#!/usr/bin/env python
# -*- coding: utf-8 -*-


def palindrome(string):
    # preprocess
    s = "^" + "#" + "#".join(string) + "#" + "$"

    c = 0
    r = 0
    p = [0] * len(s)

    for i in xrange(1,len(s)-1):
        # if P[i'] ≤ R – i, then P[i] ← P[i']
        p[i] = r > i and min(p[2 * c - i], r - i) or 0

        # Attempt to expand palindrome centered at i
        while s[i - p[i]] == s[i + p[i]]:
            p[i] += 1
        else:
            p[i] -= 1

        # else P[i] ≥ R – i
        # If palindrome centered at i expand past R, adjust center based on expanded palindrome.
        if r < p[i] + i:
            r = p[i] + i
            c = i

    return string[(p.index(max(p)) - 1 - max(p))/2 : max(p) + 1]
