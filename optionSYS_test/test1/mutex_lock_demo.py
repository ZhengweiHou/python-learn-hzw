#!/usr/bin/python
# -*- coding: UTF-8 -*-

import _thread
import threading

lock = threading.Lock()
num = 2

class producer(threading.Thread):
    def run(self):
        global  num
        times = 100000000
        while times >0  :
            lock.acquire()
            num += 1
            lock.release()
            times -= 1

class comsumer(threading.Thread):
    def run(self):
        global num
        times = 100000000
        while times >0  :
            lock.acquire()
            num -= 1
            lock.release()
            times -= 1


if __name__ == '__main__':
    print('start in main function.')
    p = producer()
    c = comsumer()
    p.start()
    c.start()

    print('Print in mian function: num = %d' % num)
    exit(0)








