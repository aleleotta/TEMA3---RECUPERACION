from threading import Thread

class MyThread(Thread):
    def __init__(self, num):
        Thread.__init__(self)
        self.num = num

    def run(self):
        print("I am the thread", self.num)