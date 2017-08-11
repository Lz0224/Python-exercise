#!/usr/bin/python
p = 'a'
o = 'b'
u = 'c'


for i in range(1,11):
    # li = range(1,i + 1)
    n = i - 1
    # ln = range(1,n + 4)
    li = [1]
    li = [li[x] + li[x + 1] for x in range(i + 1)]
