#!/usr/bin/python
# -*- coding: UTF-8 -*-

import _thread
import threading

lock = threading.Lock()
num = 0

def producer():
    global  num
    times = 100000000
    while times >0  :
        lock.acquire()
        num += 1
        lock.release()
        times -= 1

def comsumer():
    global num
    times = 100000000
    while times >0  :
        lock.acquire()
        num -= 1
        lock.release()
        times -= 1


if __name__ == '__main__':
    print('start in main function.')
    p = threading.Thread(target=producer)
    c = threading.Thread(target=comsumer)
    p.start()
    c.start()

    # p.join()
    # c.join()
    print('Print in mian function: num = %d' % num)








