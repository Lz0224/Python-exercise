# coding=utf-8

import datetime

def deco(arg):
    def begin(func):
        def war(*args, **kwarg):
            print arg
            print "现在时间"
            func(*args,**kwarg)
        return war
    return begin

@deco("hello kitty")
def getTime(a, b, c, d):
    print a, b, c, d
    print datetime.datetime.now()


getTime(1, 2, 3, 4)
