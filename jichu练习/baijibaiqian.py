#!/usr/bin/python
#coding=utf-8

# "公鸡5文钱，母鸡3文钱，小鸡1文钱3个。共买100只鸡。"
#         " 问有多少只小鸡，多少只公鸡，多少只母鸡。"

# while 循环
x = 1
y = 1

while x < 20:
    while y < 33:
        z = 100 - (x + y)
        if (z % 3 == 0) and (z / 3 + 5 * x + 3 * y == 100):
            print x, y, z

        y += 1
    x += 1
    y = 1


# for 循环


# for x in range(1,20):
#     for y in range(1,33):
#         z = 100 - (x + y)
#         if (z % 3 == 0) and (z / 3 + 5 * x + 3 * y == 100):
#             print x, y, z
