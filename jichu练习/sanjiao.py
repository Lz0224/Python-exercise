#!/usr/bin/python
p = 'a'
o = 'b'
u = 'c'

for i in range(1,11):
    li = range(1,i + 1)
    n = i - 1
    ln = range(1,n + 4)


    # ki = xi + yi
    for a in range(1,11):
        xa = li[i - 1]
        ya = ln[n + 1]
        ka = xa + ya
    q = []
    q.append(ka)
    Li = [1] + q +[1]
    # print ka, a, u
    print Li, q



    # for a in range(1,i + 1):
        # ka =xi

    # print ka, type(ka)





    # print n, ln, p
    # print i, li, o
