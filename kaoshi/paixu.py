#!/usr/bin/python
#coding=utf-8
l = [1,2,8,54,7,9,4,7,83,12,6,8,4,5,17,94,23,67]


class A(object):
    def __init__(self, l):
        self.n = len(l)

    def maopao(self, l):
        i = 0
        # n = len(l)
        while i < self.n - 1:
            j = 0
            while j < self.n - i - 1:
                if l[j] > l[j + 1]:
                    l[j],l[j + 1] = l[j + 1],l[j]
                j += 1
            i += 1

        print l


    def xuanze(self, s):
        for i in range(0, len(s) - 1):
            index = i
            for j in range(i + 1, len(s)):
                if s[index] > s[j]:
                    index = j
            s[i], s[index] = s[index], s[i]
        print s

    def charu(self, k):
        for i in range(1, len(k)):
            if k[i - 1] > k[i]:
                temp = k[i]
                n = i
                while n > 0 and k[n - 1] > temp:
                    k[n] = k[n - 1]
                    n -= 1
                k[n] = temp
        print k

class B(A):
    def kuaisu(self, l):
        left = []
        right = []
        z = []
        if len(l) <= 1:
            return l
        n = ar[len(l)/2]
        for x in l:
            if x < n:
                left.append(x)
        for x in l:
            if x > n:
                right.append(x)
        for x in l:
            if x == n:
                z.append(x)
        return kuaisu(left) + z + kuaisu(right)


a = A(l)
print a.charu(l), 'aaaa'
