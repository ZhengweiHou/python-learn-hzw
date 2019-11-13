#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import time

lock = threading.Lock()
num = 0

class producer(threading.Thread):
    def run(self):
        global  num
        times = 1000000
        while times >0  :
            # lock.acquire()
            num += 1
            # lock.release()
            times -= 1
        print("producer end!!")

class comsumer(threading.Thread):
    def run(self):
        global num
        times = 1000000
        while times >0  :
            # lock.acquire()
            num -= 1
            # lock.release()
            times -= 1
        print("comsumer end!!")


if __name__ == '__main__':
    print('start in main function.')
    p = producer()
    c = comsumer()
    p.start()
    c.start()

    p.join()    # main wait p end
    c.join()    # main wait c end

    # time.sleep(4)
    print('Print in mian function: num = %d' % num)








