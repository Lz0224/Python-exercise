#!/usr/bin/python
#coding=utf-8


def recursive(n):
    if n < 1:
        return 1
    return (n * recursive(n - 1))

i = input("Please number:    ")
r = recursive(i)

print "%d! = %d"%(i, r)
