# coding=utf-8

import socket

def server():

    # 创建
    s = socket.socket()

    # 绑定
    s.bind(('0.0.0.0',6666))

    # 监听
    s.listen(5)

    # 使用
    while True:
        c,addr = s.accept()
        print('connect addr:',addr)

        ecode_data = bytes('welcome to my course'.encode(encoding='utf-8'))

        c.send(ecode_data)
        c.close()

if __name__ == '__main__':
    server()
