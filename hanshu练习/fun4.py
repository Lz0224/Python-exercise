#!/usr/bin/python
#coding=utf-8



def fun(a, b):
    print a, b,a + b



#位置传参
fun(1, 2)


#关键字传参
fun(b = 3, a = 4)


#*传参
l = [5, 6]
fun(*l)


#**传参
d = {'b':7, 'a':8}
fun(**d)


# 
# l1 = [1, 2]
# l2 = [3, 4]
# fun(l1, l2)
