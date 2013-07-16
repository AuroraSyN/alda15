#!/usr/bin/env python
#-*- coding:utf-8 -*-

import random

def generate_array(n, range=100000):
    l = []
    while(n>0):
        l.append(random.randint(0,range))
        n -= 1
    return l
