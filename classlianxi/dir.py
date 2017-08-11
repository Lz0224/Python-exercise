# coding=utf-8
import os
import time
import shutil

# a = ['你 ', '好 ', '悠悠我心 ', '不忘初心 ', '青青子衿 ', '理想很丰满 ', '现实很骨感 ', '珠圆玉润 ', '巧夺天工 ', '妙手回春 ']
# N = 5
# M = 4
# j = 0
# print len(a)
# for n in range(1,N + 1):
#     os.mkdir("MyDir/Dir%d"%n)
#     for i in range(1,M + 1):
#         f = open('MyDir/Dir%d/file%d'%(n, i), 'w+')
#         f.write(a[j])
#         j += 1
#         if j == 10:
#             j = 0
#
# time.sleep(3)
#
# l = open('MyDir/file000', 'a+')
# for n in range(1,N + 1):
#
#     for i in range(1,M + 1):
#         # shutil.move("MyDir/Dir%d/Dir%d"%(n, i),"MyDir/dir000/")
#         f = open('MyDir/Dir%d/file%d'%(n, i), 'r+')
#         s = f.readline()
#         # s = open('MyDir/Dir%d/file%d'%(n, i), 'r+').readline()
#         # print s
#         if i == M:
#             l.write('%s\n'%s)
#         elif i == 1:
#             l.write('MyDir/Dir%d %s'%(n, s))
#         else:
#             l.write(s)
#         # l.write(s)


# 老师的。。。。。。。。。
def sj(rootDir, outPutFile):
    fw = open(outPutFile,'w+')

    for dirname in os.listdir(rootDir):
        if os.path.isdir(os.path.join(rootDir, dirname)):
            print 'process in dir:%s'%dirname
            for filename in os.listdir(os.path.join(rootDir, dirname)):
                if os.path.isfile(os.path.join(rootDir,os.path.join(rootDir, dirname))):
                    fr = open(os.path.join(rootDir,os.path.join(rootDir, dirname)), 'r+')
                    for i in fr:
                        fw.write(i)
                    fr.close()
    fw.close()


sj('mydir','newfile.txt')
