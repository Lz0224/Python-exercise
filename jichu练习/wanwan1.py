#!/usr/bin/python
#coding=utf-8



# import wanwan
#
# import sys
# sys.path.appned("/home/linux/python/python老师")
#
# import
#
#
#
# wanwan.x
#
# print wanwan.x



class Person(object):
    def __init__(self, name):
        self.name = name

    age = 14
    print age, 'aaa'

    def color(self, c):
        print "{} is {}, she is {}".format(self.name, c, self.age)



diao = Person("kitty")

# print diao.color("yello"),'bbb'
diao.color("yello")

huo = Person("gui")
huo.age = 25
Person.color(huo, "red")
