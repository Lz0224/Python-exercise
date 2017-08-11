#!/usr/bin/python


l = [[1, 6, 5, 7], [2, 5, 6, 8], [3, 6, 2, 4], [2, 4, 1, 3]]

for a in l:
    for b in a:
        print b,
    print " "

# hang = len(l)
# lie  = len(l[1])
# n    = 0
for i in l:
    ma = max(i)
    n  = i.index(ma)
    j  = 0
    mi = min(i)
    # print mi, ma, n, j

    for j in range(3):
        if l[j][n] < ma:
            # print l[j][n], 'ddd', j
            break

        # elif l[j][n] > mi:
        #     print 'aaa', j,l[j][n], n
        j += 1
    else:
        print ma, "a", j, mi
