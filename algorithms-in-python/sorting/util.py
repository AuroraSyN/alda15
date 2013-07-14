#!/usr/bin/env python
#-*- coding:utf-8 -*-

import random

def generate_array(n, range):
    l = []
    while(n>0):
        l.append(random.randint(0,range))
        n -= 1
    return l

l = generate_array(15, 200)
print l 
