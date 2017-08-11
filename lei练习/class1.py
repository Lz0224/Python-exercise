#!/usr/bin/python
#coding=utf-8



class Person(object):
    # """docstring for ."""

    #
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # print self.age, 'aaa'
    # def __init__(self, name):
    #     self.name = name

    def color(self, a = "black"):
        print "the color is %s"%a, 'pppp'



boy2 = Person("jame","23")

# boy2.age = 18
#
print boy2.age

print boy2.name

boy2.color("yello")
print "=========================================="

boy1 = Person("li lie", "12")

print boy1.age

print boy1.name

boy1.face = "帅"

print boy1.face


boy1.color("yello")
# print "============================="

print Person.color(boy2, "yello"), 'dddd'
#   不可单独实现，必须先建立个对象
# Person.age(boy2, "yello"), 'qqqq'
