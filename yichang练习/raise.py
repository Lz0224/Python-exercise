#!/sur/bin/python
#coding=utf-8

#
class MyError(Exception):
    pass

# s = raw_input()
s = "error"

try:
    if s == 'error':
        print "this is my error"
        raise MyError("no error maesage")
    else:
        print s
except MyError as e:
    print "Error message:"
    print e


# if s == 'error':
#     print "this is my error", 'aaa'
#     raise MyError("这是在哪里有错误")
# else:
#     print s,'bbb'
