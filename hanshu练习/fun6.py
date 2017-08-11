#!/usr/bin/python
#coding=utf-8


def fun(a, b = 100, *c):
    print a
    print b
    print c


fun(1, 2, 3, 4, 5)
#在Python3中可以在×c后加入普通参数，但是必须在引用时说明，
#                       或者设置默认参数,在7中演示


print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

def fun1(a, b = 100, *c, **d):
    print a
    print b
    print c
    print d

fun1(1, 2, 3, 4, 5, c = 6, d = 7)
