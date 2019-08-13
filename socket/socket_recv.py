#!/usr/bin/env python
# coding=utf-8


from socket import *
from time import ctime

HOST = '127.0.0.1'
PORT = 21002
BUFSIZ = 4
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    tcpCliSock,addr = tcpSerSock.accept()
    print('...connnecting from:', addr)

    while True:
        data = bytes(tcpCliSock.recv(BUFSIZ))
        if not data:
            break


        recvdata=data.decode()
        print('recv:%r'% recvdata)
        tcpCliSock.send(('[%s] %s' % (ctime(), data.decode())).encode())
    tcpCliSock.close()
tcpSerSock.close()

