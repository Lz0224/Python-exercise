#coding=utf-8
#闭包的概念。。。。。。。。。。。。。。。。。。。。。。。。。
a = 1
def out():
    b = 2
    def fun():
        # a += 1
        # b += 1
        print a
        print b
    return fun      #将函数当成变量返回。。。


f = out()
f()
