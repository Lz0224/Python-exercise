#!/usr/bin/python
#coding=utf-8


def fun(a, b = 100, *c, d):
    print (a)
    print (b)
    print (c)
    print (d)

fun(1, 2, 3, 4, 5, 6, b = 7)
