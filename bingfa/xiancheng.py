#!/usr/bin/python3
#  -*- coding: utf-8 -*-
import threading
import time
import os


def booth(tid):
    global i
    global lock
    while True:
        lock.acquire()
        if i != 0:
            i -= 1
            print('窗口：', tid, '剩余票数：', i)
            time.sleep(1)
        else:
            print('线程id：', tid, '没有更多的票了')
            os._exit(0)
        lock.release()
        time.sleep(1)


i = 100
lock = threading.Lock()

for k in range(10):
    new_thread = threading.Thread(target=booth, args=(k,))
    new_thread.start()
