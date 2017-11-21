#!/usr/bin/python3
#  -*- coding: utf-8 -*-
import threading
from time import ctime, sleep


def music(name):
    for i in range(2):
        print('I was listening to {0}. {1}'.format(name, ctime()))
        sleep(1)


def movie(name):
    for i in range(2):
        print('I was watching the {0}. {1}'.format(name, ctime()))
        sleep(5)


threads = []
t1 = threading.Thread(target=music, args=('带你去旅行',))
threads.append(t1)
t2 = threading.Thread(target=movie, args=('机器之血',))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()
    print('all over {}'.format(ctime()))
