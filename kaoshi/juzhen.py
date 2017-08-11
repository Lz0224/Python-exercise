#!/usr/bin/python
#coding=utf-8


l = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

k = []
n, b = 4, 3
a, j = 0, 0
for i in range(7):
    while i == 0:
        while j != 4:
            k.append(l[i][j])
            j += 1
        i += 1
    while i == 1 or i == 2:
        k.append(l[i][3])
        i += 1
    while i == 3:
        while n != 0:
            n -= 1
            k.append(l[3][n])
        i += 1
    while i == 4:
        k.append(l[i - 2][0])
        i += 1
    while i == 5:
        while a != 3:
            k.append(l[1][a])
            a += 1
            # print k, 'asddsa'
        i += 1
    while i == 6:
        while b != 1:
            b -= 1
            k.append(l[2][b])
            print k
        i += 1
    while i == 7:
        print k ,'aaa'
        break
# print k
