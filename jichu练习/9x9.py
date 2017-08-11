#!/usr/bin/python


i = 1

for i in range(1, 10):
    for j in range(i, 10):
        print ('%d * %d = %2d'%(i, j, i * j),end = ' ')
    # i += 1
    print( )
