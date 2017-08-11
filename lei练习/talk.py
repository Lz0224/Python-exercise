#!/usr/bin/python
#coding=utf-8


class Parent(object):
    """docstring for ."""
    def __init__(self, job, name):
        self.job = job
        self.__name = name


    def name(self, n):
        if n == 1:
            return self.__name
        else:
            return "sorry"


class Child(Parent):
    """docstring for ."""

a = Child("bbb", "asd")
print a.name(1)

p = Parent("aaa", "li")
print p.job

print p.name(2)
