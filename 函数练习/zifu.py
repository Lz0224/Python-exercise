#!/usr/bin/python
#coding=utf-8


a = raw_input("请输入字符：   ")
b = raw_input("请输入字符串：    ")

# a = 'l'
# b = 'hello kitty'
# print type(a), type(b)



def fun(a, b):
    c = ""
    for i in b:
        # print type(i), 'bbb'
        if i != a:
            c += i
            # print type(i), i
        elif i == a:
            print ''
    return c

print fun(a, b), 'cccc'
