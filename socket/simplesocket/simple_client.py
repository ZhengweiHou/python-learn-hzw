# coding=utf-8

import socket

def client(i):

    # 创建
    s = socket.socket()

    # 连接
    s.connect(('0.0.0.0',6666))

    print('Recv msg:%s,client:%d' %(s.recv(1024),i))

    s.close()


if __name__ == '__main__':
    for i in range(10):
        client(i)