#!/usr/bin/python
#coding=utf-8


l = [[1, 2, 3, 4, 4], [1, 2, 3, 4, 4], [2,5, 6, 7, 8], [9, 4,10, 11, 12], [13, 14, 24, 15, 16]]
# l = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

def snail(l):
    return list(l[0]) + snail(zip(*l[1:])[::-1]) if l else []


print snail(l)
# print *l[1:]
