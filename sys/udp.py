#!/usr/bin/python
#coding=utf-8

import  threading
from socket import *
import sys


def sock(data, addr):

    print "from %s : %s"%(addr, data)


def thread(a):
    e = threading.Event()
    w1 = threading.Thread(target = sock, args = (e, data, addr))
    w1.start()


print "等待连接。。。"
while 1:
    HOST = '192.168.0.135'
    PORT = 8888
    ADDR = (HOST, PORT)

    s = socket(AF_INET, SOCK_DGRAM)

    name = raw_input("Please your nickname >>>")

    s.sendto('%s : '%name,ADDR)

    # print "连接来自于 ：",addr

    thread(data, addr)
