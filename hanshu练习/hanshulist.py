#!/usr/bin/python
#coding=utf-8

l = [input("Please")]
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# l = [1, 2, 3, 4]

def fun(l):
    l1 = []
    l2 = []
    for i in range(len(l)):
        if l[i] % 2 == 1:
            l1.append(l[i])
        elif l[i] % 2 == 0:
            l2.append(l[i])
    print l1 + l2

fun(l)



# def fun():
#     l1 = []
#     l2 = []
#     for i in l:
#         if i % 2 == 1:
#             l1.append(i)
#             print(l1)
#         elif i % 2 == 0:
#             l2.append(i)
#             print(l2)
#     print l1 + l2



# fun()
