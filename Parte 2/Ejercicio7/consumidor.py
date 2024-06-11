from threading import Thread, Condition
from queue import Queue
import time
from random import randint

class Consumidor(Thread):

    def __init__(self, name, cond: Condition, queue: Queue):
        Thread.__init__(self, name = name)
        self.cond = cond
        self.queue = queue
    
    def run(self):
        while(True):
            with self.cond:
                while self.queue.empty():
                    print(f"{self.name} esta esperando datos para consumir.")
                    self.cond.wait()
                time.sleep(randint(1,5))
                obj = self.queue.get()
                print(f"{self.name} esta consumiendo {obj}.")
                self.cond.notifyAll()