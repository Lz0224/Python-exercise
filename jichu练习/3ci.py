#!/usr/bin/python
#coding=utf-8

# a = 4
# n = 3
# if循环方法
# i = input('Please num:1~9    ')
# if i == a :
#     print "very good"
# elif i != a:
#     i = input('Please num:1~9    ')
#     if i == a :
#         print "very good"
#     elif i != a:
#         i = input('Please num:1~9    ')
#         if i == a :
#             print "very good"
#         elif i != a:
#             print  "Game over"
# else:
#     print "Please 1~9 "

#while循环法
# while n != 0:
#     i = input("Please num:1~9    ")
#     if i == a:
#         break
#         print "very good"
#     elif i != a:
#         n -= 1
# else:
#     print "Game over"

#函数方法
# def mima(n):
#     # n = 3
#     i = input("Please num:1~9    ")
#     if i == a :
#         print "very good"
#     elif i != a and n != 0:
#         n -= 1
#         mima(n)
#     # elif i != a and n == 0:
#     elif i != a:
#         print "Game over"
#     else:
#         print 'hello kitty'
# # a = input("Please mima:    ")
# a = 4
# n = 2
# mima(n)


def ask_ok(prompt, retries = 3, complaint = 'Yes or no, Please!'):
    while True:
        ok = input(prompt)
        if ok == a:
            print "Very good"
            break
        if ok != a and retries > 0:
            print complaint
            retries -= 1
        if retries == 0:
            # raise IOError('refusenik user')
            print "Game over"
            return False
        # print complaint
a = 4
ask_ok('Please num:1~9    ')
