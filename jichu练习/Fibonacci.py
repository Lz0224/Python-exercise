#!/usr/bin/python
#coding=utf-8


x = 0
y = 1

l = []

while y < 1000:
    x, y = y, x + y
    l.extend([x, y])
else:
    print l
    print  "哈哈哈"
