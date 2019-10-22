#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import time

lock = threading.Lock()
num = 0

def producer():
    global  num

    times = 1000000
    while times >0  :
        global lock
        if lock.acquire():
            num += 1
            lock.release()
            times -= 1
    print('producer end!!')

def comsumer():
    global num
    times = 1000000
    while times >0  :
        global lock
        if lock.acquire():
            num -= 1
            lock.release()
            times -= 1
    print('comsumer end!!')


if __name__ == '__main__':
    print('start in main function.')
    p = threading.Thread(target=producer)
    c = threading.Thread(target=comsumer)
    p.start()
    c.start()

    time.sleep(3)
    print('Print in mian function: num = %d' % num)








