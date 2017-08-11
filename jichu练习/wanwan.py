#!/usr/bin/python
#coding=utf-8

# def wanwan():
#     """
#         人生苦短
#         我用Python
#
#    """
#
#
#
#
# url = "https://tieba.baidu.com/p/2460150866"
# def get_html():
#     page = urllib.urlopen(url)



l = []

for i in range(15):
    l.append([])
    l[i].append(1)
    for j in range(1, i + 1):
        l[i].append(l[i - 1][j - 1] + l[i - 1][j])
    l[i].append(0)

for i in l:
    i.pop()
    print i



# l = []
#
# for i in range(15):
#     l.append([])
#     l[i].append(1)
#     for j in range(1,i + 1):
#         l[i].append(l[i - 1][j - 1] + l[i - 1][j])
#     l[i].append(0)
#
# for i in l:
#     i.pop()
#     print i











































# class One(object):
#     __name = "ghjgj"
#
#     def get_naem(self):
#         return self.__name
#         pass
#
#     def set_naem(self):
#         self.__name = "adasd"
#         pass
#
# o = One()
#
# o.set_naem()
#
# print o.get_naem()
