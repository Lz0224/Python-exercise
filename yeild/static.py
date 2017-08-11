#coding=utf-8

class Parent(object):
    @staticmethod
    def foo():
        print "静态方法"


class Child(Parent):
    pass


static = Parent()

static.foo()
Parent.foo()

Child.foo()
