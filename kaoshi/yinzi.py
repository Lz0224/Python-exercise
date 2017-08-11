#!/usr/bin/python
#coding=utf-8

class MyError(Exception):
    pass

N = input('请输入1以上的数字：   ')
if N <= 1:
    raise MyError("输入错误。。。")

def choushu(a):
    while a % 5 == 0:
        a /= 5
    while a % 2 == 0:
        a /= 2
    while a % 3 == 0:
        a /= 3
    if a == 1:
        return True
    else:
        return False

l = []

for i in range(1,1000):
    if choushu(i):
        l.append(i)

print l[N]
