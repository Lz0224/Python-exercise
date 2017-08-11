#!/usr/bin/python
#coding=utf-8#!


a = 5
b = 6
def fun():
    global a, b
    a += 1
    b += 1
    print a, b

    c, d = 1, 2
    return locals()

fun()
# print fun()
print a

print globals()
