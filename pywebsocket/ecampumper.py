import threading
import time

import logging

import xhsi


class ecampumper(object):

    def __init__(self):

        self.die = threading.Event()
        self.lock = threading.Lock()
        self.websocketThread = False
        self.xhsiThread = False

        self.die.clear()

        
        self.client = xhsi.xhsiRx()
        
        if not self.xhsiThread:
            self.xhsiThread = threading.Thread(target=self.xhsiStart)
            self.xhsiThread.start()

    def setobserver(self,x):
        self.client.setobs(x)
        
    def acquireLock():
        self.lock.acquire()

    def releaseLock():
        self.lock.release()
        
    ##### websocket thread #####

    def xhsiStart(self):
        
        self.client.network()
        self.client.forever1()

if __name__ == "__main__":

    def f():
        print 'oi'
        
    e = ecampumper()
    e.setobserver(f)
    
