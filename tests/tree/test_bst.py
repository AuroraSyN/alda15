#!/usr/bin/env python
# -*- coding: utf-8 -*-


from algorithms_in_python.tree.binary_search_tree import build_tree


array = [8, 3, 10, 1, 6, 4, 7, 14, 13]

pre_order = [8, 3, 1, 6, 4, 7, 10, 14, 13]
in_order = [1, 3, 4, 6, 7, 8, 10, 13, 14]
post_order = [1, 4, 7, 6, 3, 13, 14, 10, 8]


def test_build_tree():
    root = build_tree(array[:])
    assert root.data == 8
    assert root.left.data == 3
    assert root.left.left.data == 1
    assert root.left.right.data == 6
    assert root.left.right.left.data == 4
    assert root.left.right.right.data == 7
    assert root.right.data == 10
    assert root.right.right.data == 14
    assert root.right.right.left.data == 13
    assert root.left.left.left is None
    assert root.left.left.right is None
    assert root.left.right.left.left is None
    assert root.left.right.left.right is None
    assert root.left.right.right.left is None
    assert root.left.right.right.right is None
    assert root.right.left is None
    assert root.right.right.right is None
    assert root.right.right.left.left is None
    assert root.right.right.left.right is None


def test_preorder_travel():
    root = build_tree(array[:])
    assert pre_order == root.preorder_travel()


def test_inorder_travel():
    root = build_tree(array[:])
    assert in_order == root.inorder_travel()


def test_postorder_travel():
    root = build_tree(array[:])
    assert post_order == root.postorder_travel()


def test_search():
    root = build_tree(array[:])
    node, parent = root.search(6)
    assert node.left.data == 4
    assert node.right.data == 7
    assert parent.data == 3


def test_compare():
    tree1 = build_tree(array[:])
    tree2 = build_tree(array[:])
    tree3 = build_tree(post_order[:])
    assert True == tree1.compare(tree2)
    assert False == tree1.compare(tree3)


def test_count_children():
    root = build_tree(array[:])
    node, parent = root.search(10)
    assert 2 == root.count_children()
    assert 1 == node.count_children()
    assert 0 == node.right.left.count_children()


def test_delete():
    root = build_tree(array[:])
    root.delete(1)
    assert [8, 3, 6, 4, 7, 10, 14, 13] == root.preorder_travel([])
    root = build_tree(array[:])
    root.delete(14)
    assert [8, 3, 1, 6, 4, 7, 10, 13] == root.preorder_travel([])
    root = build_tree(array[:])
    root.delete(3)
    assert [8, 4, 1, 6, 7, 10, 14, 13] == root.preorder_travel([])
    root = build_tree(array[:])
    root.delete(6)
    assert [8, 3, 1, 7, 4, 10, 14, 13] == root.preorder_travel([])
    root = build_tree(array[:])
    root.delete(8)
    assert [10, 3, 1, 6, 4, 7, 14, 13] == root.preorder_travel([])
