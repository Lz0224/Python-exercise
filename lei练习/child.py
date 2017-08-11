#!/usr/bin/python
#coding=utf-8


class ParentClass(object):
    """docstring for ParentClass."""
    name = "老张"
    # def __init__(self, arg):
    #     super(ParentClass, self).__init__()
    #     self.arg = arg
    def fun(self):
        print "老子有钱"

class ChildClass(ParentClass):
    """这是什么玩意。。。。"""
    # def __init__(self, arg):
    #     super(, self).__init__()
    #     self.arg = arg
    def fun1(self):
        print "哥也有钱"

class GrentChildClass(ChildClass):
    pass


child = ChildClass()

print child.name

child.fun()

grent_child = GrentChildClass()

print grent_child.name

print dir(ParentClass)
print ChildClass.__doc__
