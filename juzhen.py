#!/usr/bin/python


k = [(1, 3, 5, 7), (2, 4, 6, 8), (5, 6, 2, 4), (2, 6, 1, 3)]

# i = range(1,len(array) + 1)
# i = 0
for i in range(len(k)):
    l = k[i]
    print l, i,'aaa'
    a = max(l)
    print a, 'bbb'

#
#
#
# l1 = zip(array[x] for x in range(len(l1)))
#
#     k = l1[x-1]
#     b = max(k)
#     print b
#
#
#
#
#
# print l1
#
#
#
#
# print type(l1[0])


#
l  = k[0]
l1 = k[1]
l2 = k[2]
l3 = k[3]
a = max(l)
b = max(l1)
c = max(l2)
d = max(l3)
l5 = zip(l, l1, l2, l3)
l6 = zip(*k[::-1])
# print  a, b, c, d, l5, l6
print l, l1, l2, l3
