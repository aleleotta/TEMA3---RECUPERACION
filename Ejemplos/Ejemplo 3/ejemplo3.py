from threading import Thread, Semaphore

class MyThread(Thread):

    def __init__(self, name):
        Thread.__init__(self, name = name)

    def run(self):
        pass