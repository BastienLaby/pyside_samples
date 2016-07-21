#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import threading
import Queue

from PySide import QtCore, QtGui, QtOpenGL


def processData(data):
    print "process data '%s'" % data


class CustomThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.id = threadID
        self.name = name
        self.counter = counter

    def run(self):
        threadLock.acquire()
        print "Start thread " + self.name
        printTime(self.name, self.counter, 5)
        print "Stop thread " + self.name
        threadLock.release()


if __name__ == '__main__':

    images = ["image" + str(i+1) for i in range(10)]

    queue = Queue.Queue()

    threads = []
    threadCount = 3
    for i in range(threadCount):
        threads.append(CustomThread)

    # thread1 = CustomThread(1, "thread1", 0.66)
    # thread2 = CustomThread(2, "thread2", 1.34)

    
    print images
    # thread1.start()
    # thread2.start()