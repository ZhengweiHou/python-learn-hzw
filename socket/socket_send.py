#!/usr/bin/env python
# coding=utf-8

from socket import *

HOST = '127.0.0.1' # or 'localhost'
PORT = 21002
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)

# tcpCliSock = socket(AF_UNIX,SOCK_STREAM)

tcpCliSock.connect(ADDR)
while True:
     data1 = input('>')

     ecode_data = bytes(data1.encode(encoding='utf-8'))

     print("messageleng:%r"%ecode_data.__len__())

     if not data1:
         break

     tcpCliSock.send(ecode_data)

     data1 = tcpCliSock.recv(BUFSIZ)
     if not data1:
         break
     print(data1.decode('utf-8'))
tcpCliSock.close()
