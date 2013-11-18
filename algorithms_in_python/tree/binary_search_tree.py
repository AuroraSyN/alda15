#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Binary Search Tree


class bst(object):
    """
    BST node:
      contains a left child, a right child and a data object
    """
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        """
        insert a node with data
        """
        # if the data object you want to insert is smaller than
        # the data object held in current node
        if data < self.data:
            # if current node doesn't have a left child
            if self.left is None:
                # create a new node with the data then attach it
                # to the current node as its left child
                self.left = bst(data)
            else:
                #enter the current node's left sub-tree
                self.left.insert(data)
        # check may enter this part if input data
        # is larger than the data in current node
        else:
            # similar check as in left sub-tree
            if self.right is None:
                self.right = bst(data)
            else:
                self.right.insert(data)

    def delete(self, data):
        """
        Delete note with given data
        """
        node, parent = self.search(data)
        if not node:
            return None
        else:
            children_num = node.count_children()
            # if node has no children, just remove it
            if children_num == 0:
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
                del node
            # if node has one child, replace it by its child
            elif children_num == 1:
                if node.left:
                    n = node.left
                else:
                    n = node.right
                if parent.left is node:
                    parent.left = n
                if parent.right is node:
                    parent.right = n
                del node
            # if node has 2 children
            else:
                # find its successor
                successor = node.right
                while successor.left:
                    successor = successor.left
                n, p = self.search(successor.data)
                # replace node data with its successor's data
                node.data = successor.data
                # fix bst
                if successor.right:
                    node.right = successor.right
                if p is node:
                    p.right = successor.right
                    successor = None
                elif successor.data < p.data:
                    p.left = None
                else:
                    p.right = None

    def search(self, data, parent=None):
        """
        Search data in given node
        """
        if data < self.data:
            if self.left is None:
                # return None to break searching
                return None, None
            # enter left sub-tree
            return self.left.search(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            # enter right sub-tree
            return self.right.search(data, self)
        # value matched
        else:
            return self, parent

    def preorder_travel(self, output=[]):
        """
        travel tree pre-order
        """
        output.append(self.data)
        if self.left:
            self.left.preorder_travel(output)
        if self.right:
            self.right.preorder_travel(output)
        return output

    def inorder_travel(self, output=[]):
        """
        travel tree in-order
        """
        if self.left:
            self.left.inorder_travel(output)
        output.append(self.data)
        if self.right:
            self.right.inorder_travel(output)
        return output

    def postorder_travel(self, output=[]):
        """
        travel tree post-order
        """
        if self.left:
            self.left.postorder_travel(output)
        if self.right:
            self.right.postorder_travel(output)
        output.append(self.data)
        return output

    def compare(self, tree_node):
        """
        compare two tree
        """
        if not tree_node:
            return False
        if self.data != tree_node.data:
            return False
        flag = True
        if not self.left:
            if tree_node.left:
                return False
        else:
            flag = self.left.compare(tree_node.left)
        if not self.right:
            if tree_node.right:
                return False
        else:
            flag = self.right.compare(tree_node.right)
        return flag

    def count_children(self):
        """
        Return the number of children of the given node
        """
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count


def build_tree(array):
    """
    build the binary search tree from array
    """
    root = bst(array.pop(0))
    for item in array:
        root.insert(item)
    return root
