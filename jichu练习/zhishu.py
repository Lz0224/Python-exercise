#!/usr/bin/python

a = 'a'
b = 'b'
c = 'c'
d = 'd'

l = []

for i in range(1,101):
    n = 0
    for x in range(1,i + 1):
        # print i, x, c
        # while i % x == 0 and n < 5:
        if i % x == 0:
            n += 1
            # l.append(x)
            # continue
            # print i, x, n, a
        else:
            continue
    # if len(l) == 2:
    if n == 2:
        print i, b
            # break
            #     continue
            # else:
            #     continue
        # else:
        #     n = 0
