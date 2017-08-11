#!/usr/bin/python
#coding=utf-8


class TreeNode(object):
    def __init__(self):
        self.data = '#'
        self.Lchild = None
        self.Rchild = None

class Tree(TreeNode):
    def create_tree(self, tree):
        data = raw_input('-->>>')
        if data == '#':
            tree = None
        else:
            tree.data = data
            tree.Lchild = TreeNode()
            self.create_tree(tree.Lchild)
            tree.Rchild = TreeNode
            self.create_tree(tree.Rchild)

    def visit(self, tree):
        if tree.data is not '#':
            # print str(tree.data) + '\t',
            print 'sss'


    def pre_order(self, tree):
        if tree is not None:
            self.visit(tree)
            self.pre_order(tree.Lchild)
            self.pre_order(tree.Rchild)

    def in_order(self, tree):
        if tree is not None:
            self.in_order(tree.Lchild)
            self.visit(tree)
            self.in_order(tree.Rchild)

    def post_order(self, tree):
        if tree is not None:
            self.post_order(tree,Lchild)
            self.post_order(tree.Rchild)
            self.visit(tree)



t = TreeNode()
tree = Tree()

tree.create_tree(t)
tree.pre_order(t)
print '\n'
tree.in_order(t)
print '\n'
tree.post_order(t)
