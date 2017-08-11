#!/usr/bin/python
#coding=utf-8

# from random import *
import random


# l = []
# i = 0
#
# while i <= 5:
#     i += 1
#     b = random.randint(1, 33)
#     print b
#     l.append(b)
# print l
# l.sort()
# a = random.randint(1,16)
# l.append(a)
# print l
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
l = random.sample(range(1,34),6)

l.sort()
# l.append(random.randint(1,17))
# print l
print l, random.randint(1,16)
