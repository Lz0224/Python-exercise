# coding=utf-8
import os
import time

filename = raw_input("请输入文件名字 :   ")

filestat = os.stat(filename)

print filestat

print time.localtime(filestat.st_ctime)
