#coding=utf-8
import datetime
#类的装饰器

class Deco(object):
    def __init__(self,obj):
        self.func = obj

    def __call__(self,*args,**wkarg):
        print "现在时间：    "
        self.func(*args,**wkarg)
@Deco          #装饰器的应用
def getTime(w,s,g,q):
    print w,s,g,q
    print datetime.datetime.now()


getTime(1,2,3,4)
