# coding=utf-8

import sys


with open('file','a+') as f:
    print >>f,"塞翁失马，焉知非福"

print >>sys.stdout,"输出"
print >>sys.stderr,"出错"
# print >>sys.stdin,"输入"
