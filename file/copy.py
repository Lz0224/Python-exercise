# coding=utf-8

try:
    f = open('3.jpg','r+')
    f1 = open('/home/linux/python/3.jpg', 'w+')
except:
    print "出错啦～～～"

while True:
    s = f.readline(1)
    if not s:
        break
    f1.write(s)
print 'aaaa'
