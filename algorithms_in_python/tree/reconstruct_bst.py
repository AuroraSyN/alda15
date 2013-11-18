#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Reconstruct Binary Tree
from binary_search_tree import bst, build_tree


def reconstruct1(pre, ino, root):
    """
    Reconstruct the tree with preorder and inorder traversal result.
    """
    if len(pre) == 0 or len(ino) == 0:
        return None
    if len(pre) == 1 or len(ino) == 1:
        return bst(pre[0])
    # infer root from preorder
    root = bst(pre[0])
    # separate inorder into left and right children by root index
    in_left = ino[:ino.index(pre[0])]
    in_right = ino[ino.index(pre[0]) + 1:]
    # separate preorder into left and right children by length of inorder list
    pre_left = pre[1: len(in_left) + 1]
    pre_right = pre[len(in_left) + 1:]
    # reconstruct the tree recursively
    root.left = reconstruct1(pre_left, in_left, root)
    root.right = reconstruct1(pre_right, in_right, root)
    return root


def reconstruct2(post, ino, root):
    """
    Reconstruct the tree with postorder and inorder traversal result.
    """
    if len(post) == 0 or len(ino) == 0:
        return None
    if len(post) == 1 or len(ino) == 1:
        return bst(post[-1])
    # infer root from postorder
    root = bst(post[-1])
    # separate inorder into left and right children by root index
    in_left = ino[:ino.index(post[-1])]
    in_right = ino[ino.index(post[-1]) + 1:]
    # separate postorder into left and right children by length of inorder list
    post_left = post[:len(in_left)]
    post_right = post[len(in_left):-1]
    root.left = reconstruct2(post_left, in_left, root)
    root.right = reconstruct2(post_right, in_right, root)
    return root
