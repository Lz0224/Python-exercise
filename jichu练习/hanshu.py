#!/usr/bin/python

def funq(x):
    return x ** 3

def funw(x):
    return x > 2 and x < 7

def fune(x,y):
    return x * y


l = [1, 2, 3, 4, 5, 6, 7, 8, 9]


print map(funq, l)

print filter(funw, l)

print reduce(fune, l)
