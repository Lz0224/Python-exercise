#!/usr/bin/python
#coding=utf-8


def fil(n):
    a, b = 0, 1
    while a < n:
        # print a
        yield a
        a, b = b, a + b
        # print a
        # print a
l = []
for i in fil(40):
    # l.append(i)
    print i

# print l
# print fil(5),type(fil(5))



# def fun1():
#     m = yield
#     print "+++++",m
#     n = yield 666
#     print "-----",n
#     a = yield
#     print "!!!!!",a
# fun1()
# fun1().next()
# fun1().send(888)
# fun1().next()
