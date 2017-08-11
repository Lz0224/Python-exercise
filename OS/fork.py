#coding=utf-8
import os
import  time


#用fork模块创建进程。。。pid为正整数父进程的。。。。pid为0时它是子进程，pid为负整数时它创建子进程失败。
pid = os.fork()

if pid < 0:
    print "创建进程失败"
elif pid == 0:
    print time.clock(), 'aaa'
    print "创建子进程成功"

else:
    # time.sleep(1)
    print time.clock(), 'bbb'
    print "创建父进程成功"

print time.clock(), 'AAA'


print "+++++++++++++++++++++++++"
