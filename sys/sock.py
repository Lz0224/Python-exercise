#!/usr/bin/python
#coding=utf-8


from socket import *
from time import ctime
import sys

HOST = '192.168.0.135'
PORT = int(sys.argv[1])
BUFSIZE = 1024
ADDR = (HOST, PORT)

sockfd = socket(AF_INET, SOCK_STREAM)

sockfd.bind(ADDR)

sockfd.listen(5)

while 1:
    print "等待连接。。。。。。。。。"

    connfd, addr = sockfd.accept()

    print "连接来自于 :",addr

    while 1:
        data = connfd.recv(BUFSIZE)
        print "来自%s ：  %s"%(addr,data)
        if data[:4] == "quit":
            break
        connfd.send("[%s] : %s"%(ctime(), data))


sockfd.close()
connfd.close()
