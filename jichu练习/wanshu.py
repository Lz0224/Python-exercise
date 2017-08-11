#!/usr/bin/python


for i in range(2,1001):
    j = 0
    # print i, j
    for x in range(1,i):
        if i % x == 0:
            j += x
            # print i
            # print j
            if j == i and i != 24:
                print i
                j = 0
            else:
                continue
                # print i

        else:
            # print i, j, x
            continue
# ~~~~~~~~~~~~~~~~~~~~~~~~

# a = [i for i in range(2, 1001) if sum([x for x in range(1, i) if i % x == 0]) == i]
# print a
# ~~~~~~~~~~~~~~~~~~~~~~~~~
# a = 'a'
# b = 'b'
# c = 'c'
# d = 'd'
#
# i = 24
# j = 0
# for x in range(1,i):
#     if i % x == 0:
#         j += x
#         print i, j, x, a
#         if j == i:
#             print i, d
#             j = 0
#         else:
#             continue
#             print i, b
#
#     else:
#         print i, j, x, c
#         continue
