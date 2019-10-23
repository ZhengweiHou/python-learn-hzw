#!/usr/bin/python
# -*- coding: UTF-8 -*-
import threading

lock = threading.Lock()
num = 0

def producer():
    global  num
    times = 1000000
    while times >0  :
        global lock
        # lock.acquire()
        num += 1
        # lock.release()
        times -= 1
    print('producer end!!')

def comsumer():
    global num
    times = 1000000
    while times >0  :
        global lock
        # lock.acquire()
        num -= 1
        # lock.release()
        times -= 1
    print('comsumer end!!')

if __name__ == '__main__':
    print('start in main function.')
    p = threading.Thread(target=producer)
    c = threading.Thread(target=comsumer)
    p.start()
    c.start()

    p.join()    # main wait p end
    c.join()    # main wait c end
    print('Print in mian function: num = %d' % num)








