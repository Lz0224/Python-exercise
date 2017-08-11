#!/usr/bin/python

#coding=utf-8



for i in range(100,1001):
    a = i/100               #百位数值
    b = (i/10)%10           #十位数值
    c = i%10                #个位数值
    if a ** 3 + b ** 3 +c ** 3 == i:
        print i


# i/100 ** 3 + (i/10)%10 ** 3 + i%10 ** 3)
# == int(str(range(100,1001)))
