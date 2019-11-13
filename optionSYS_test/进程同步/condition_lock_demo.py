#!/usr/bin/python
# -*- coding: UTF-8 -*-
import threading
import time

mutex_lock = threading.Lock()
con_lock = threading.Condition()
num = 0
MAX_BUF=5

def producer():
    global  num,MAX_BUF,con_lock
    while True:

        # mutex_lock.acquire()

        while num >= MAX_BUF:
            print("[P]缓冲区满了，等待消费者消费...")
            print('[P]通知消费者...')
            con_lock.notify()
            con_lock.wait()

        num += 1
        time.sleep(1)
        print('[P]生产一个产品，当前产品数： %d' % num)





def comsumer():
    global  num,MAX_BUF,con_lock
    while True:
        while num <= 0:
            print("[C]缓冲区空了，等待生产者生产...")
            print('[C]通知生产者...')
            con_lock.notify()
            con_lock.wait()

        num -= 1
        time.sleep(1)
        print('[C]消费一个产品，当前产品数： %d' % num)



if __name__ == '__main__':
    print('start in main function.')
    p = threading.Thread(target=producer)
    c = threading.Thread(target=comsumer)
    p.start()
    c.start()
    p.join()    # main wait p end
    c.join()    # main wait c end
    # print('Print in mian function: num = %d' % num)

# 输出：
# start in main function.
# producer end!!
# comsumer end!!
# Print in mian function: num = 0

