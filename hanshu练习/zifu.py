#!/usr/bin/python
#coding=utf-8


# a = raw_input("请输入字符：   ")
# b = raw_input("请输入字符串：    ")

a = ' '
b = 'My name is Li Zhe'
# print type(a), type(b)



# def fun(a, b):
#     c = ""
#     for i in b:
#         # print type(i), 'bbb'
#         if i != a:
#             c += i
#             # print type(i), i
#         elif i == a:
#             c += '%20'
#             # print ' '
#     return c
#
# print fun(a, b), 'cccc'




def fun(a, b):
    c = ""
    for i in b:
        # print type(i), 'bbb'
        if i == a:
            i = "%20"
        c += i
    return c



print fun(a, b)
