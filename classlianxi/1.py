# coding=utf-8
import time
import datetime

# f = open('test.txt','a+')
#
# a = datetime.datetime.now()
#
# f.write(' ')
# n = f.tell() / 31 + 1
#
#
# while True:
#     n = f.tell() / 31 + 1
#
#     time.sleep(1)
#     f.write("%d , %s\n"%(n, a))
# f.close()
# 老师的。。。
line = 0

k = open('time.txt', 'a+')

for i in k:
    line += 1

while True:
    tm = time.localtime()
    line += 1
    time.sleep(1)
    print >>k,"%d, %4d-%02d-%02d %02d:%02d:%02d"%(line, tm.tm_year, tm.tm_mon, tm.tm_mday, tm.tm_hour, tm.tm_min, tm.tm_sec)
    k.flush()
k.close()
