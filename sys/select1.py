#!/usr/bin/python
from socket import *
from time import ctime
import sys
from select import *

HOST = '192.168.0.135'
PORT = 8888
ADDR = (HOST, PORT)

sockfd = socket(AF_INET, SOCK_STREAM)
sockfd.bind(ADDR)
sockfd.listen(5)

inputs = [sockfd]

while 1:
    rs, ws, es = select(inputs, [], [])
    for r in rs:
        if r is sockfd:
            connfd, addr = sockfd.accept()
            print("connected from : ", addr)
            inputs.append(connfd)
        else:
            try:
                data = r.recv(BUFSIZE).decode()
                disconnect = not data
            except socket.error:
                disconnect = True
            if disconnect:
                print(r.getpeername(), 'discoonected')
                inputs.remove(r)
                r.close()
            else:
                r.send(('[%s] :%s'%(ctime(), data)).encode())

sockfd.close()
