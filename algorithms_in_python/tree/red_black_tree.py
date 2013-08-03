#!/usr/bin/env python
# -*- coding: utf-8 -*-


class node(object):
    """ a red-black tree node."""
    def __init__(data):
        self.data = data
        self.color = 'r'
        self.left = None
        self.right = None
        self.parent = None


def left_rotate(tree, x):
    """ left rotation of red-black tree."""
    y = x.right
    x.right = y.left
    if y.left is not None:
        y.left.parent = x
    y.parent = x.parent
    if x.parent == None:
        tree = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.left = x
    x.parent = y
