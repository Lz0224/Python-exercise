#coding=utf-8

import datetime

def begin(func):
    def wrapper():
        print "现在时间:    "
        func()
    return wrapper       #闭包作用  。。。。注：此处没有()，他是一个变量(也可以称之为一个对象)

@begin          #装饰器的应用
def getTime():
    print datetime.datetime.now()

# getTime()
#
# begin(getTime)()


def deco(deco):
    def begin(func):
        def wrapper(*a, **b):
            print deco
            print "现在时间:    "
            func(*a, **b)
        return wrapper
    return begin

@deco('deco')          #装饰器的应用
def getTime(w,s,g,q):
    print w,s,g,q
    print datetime.datetime.now()

getTime(1,2,3,4)
