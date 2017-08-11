#coding=utf-8

#hasattr    getattr     setattr     delattr
#isinstance issubclass


class Parent(object):
    name = '父类'


class Child(Parent):
    age = 23
    name1 = '子类'



p = Child()

print issubclass(Child, Parent)
print isinstance(p, Parent)
print "~~~~~~~~~~~~"
# setattr(p,'sex','m')
p.sex = 'm'
delattr(p, 'name1')
print p.sex
