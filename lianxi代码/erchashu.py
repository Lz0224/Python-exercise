#!/usr/bin/python
#coding=utf-8

'''
        created bu zwg in 2017-7-8
'''

import copy

class node(object):
    def __init__(self, name, data):
        self.data = data
        self.name = name
        self.Rchild = None
        self.Lchild = None
        self.child_number = 0
        self.parent = None

    def add_Rchild(self, node):
        if self.Rchild is not None:
            self.Rchild = node
        else:
            self.Rchild = node
            self.child_number += 1
        node.set_parent(self)
    def drop_Rchild(self):
        self.Rchild = None
        self.child_number -= 1

    def set_parent(self, node):
        self.parent = node

    def add_Lchild(self, node):
        if self.Lchild is not None:
            self.Lchild = node
        else:
            self.Lchild = node
            self.child_number += 1
        node.set_parent(self)
    def drop_Lchild(self):
        self.Lchild = None
        self.child_number -= 1



class tree(object):
    def __init__(self, node):
        self.parent = node
        self.depth = 1
        self.all_node =用递归访问子节 {node.name:node}
        self.enable_node = {node.name:node}
        c1 = node.Rchild
        c2 = node.Lchild
        C  = [c1, c2]
        B  = [i for i in C if i is not None]
        if len(B) == 2:
            del self.enable_node[node.name]
        while len(B) != 0:
            self.depth += 1
            C = copy.copy(B)
            for i in B:
                C.remove(i)
                if i.Rchild is not None:
                    C.append(i.Rchild)
                if i.Lchild is not None:
                    C.append(i.Lchild)
