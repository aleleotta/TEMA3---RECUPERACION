from threading import Thread, Lock
from random import randint

class MyThread(Thread):

    list = [False, False, False, False, False]
    lock = Lock()

    def __init__(self, name):
        Thread.__init__(self, name = name)

    def run(self):
        print(f"{self.name} started executing.")
        pos = randint(0, 4)
        print(f"{self.name} wants to access position {pos}.")
        MyThread.lock.acquire()
        if not MyThread.list[pos]:
            print(f"{self.name} takes position {pos}")
            MyThread.list[pos] = True
        else:
            print(f"{self.name} tries to take position {pos} but is not successful.")
        MyThread.lock.release()
