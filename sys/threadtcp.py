from socket import *
from time import ctime
import sys
from SocketServer import ThreadingTCPServer


HOST = '192.168.0.135'
PORT = int(sys.argv[1])
BUFSIZE = 1024
ADDR = (HOST, PORT)
