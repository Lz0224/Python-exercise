#!/usr/bin/python
#coding=utf-8

l = []


for i in range(10):
    l.append([])
    l[i].append(1)
    for j in range(1, i + 1):
        l[i].append(l[i - 1][j - 1] + l[i - 1][j])
    l[i].append(0)


for i in l:
    i.pop()
    print i
