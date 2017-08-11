#!/usr/bin/python
#coding=utf-8
# N = raw_input("请输入字母或者数字:   ")

class MyError(Exception):
    pass

def addrs(*a):
    try:
        for n in a:
            if type(n) == int:
                l = 0
            elif type(n) == str:
                l = ""
            else:
                raise MyError("什么玩意，输入错误。")
        for i in a:

            l += i
            # l += a[i]
            # print type(i),type(a),type(l)
        print a, l,
    except TypeError as e:
        print e,'请输入全为数字或者字母'

# addrs('d','d','g','ggawr','ew','tgerw','t','rt','we')
# addrs(1,2,3,4,56,7,8,9,7,5,43,32,46,6)
addrs(1,2,'3',4,56,7,8,9,7,5,43,32,46,'b')
# addrs(N)
