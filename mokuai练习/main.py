#!/usr/bin/python
#coding=utf-8



import dir1.module1  as m #导入模块module1
#将模块中的函数 类 变量导入到本地。即此空间内，并不可重复命名
from dir1.module2 import C
reload(m)      #重新导入模块module1

# print module1.a

obj = m.A()

obj.a()

m.b()

a = 10


print m.__doc__

print m.a
