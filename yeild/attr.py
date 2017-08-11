class A(object):
    def __getattr__(self,name):
        print "You use getattr"
        return "No"

    def __setattr__(self,name,value):
        print "You use setattr"
        self.__dict__[name] = value


a = A()

# a.d
print a.k
a.x ='set x'
