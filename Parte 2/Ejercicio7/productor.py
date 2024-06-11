from threading import Thread, Condition
from queue import Queue

class Productor(Thread):

    def __init__(self, name, cond: Condition, queue: Queue):
        Thread.__init__(self, name = name)
        self.cond = cond
        self.queue = queue

    def run(self):
        #while(True):
            with self.cond:
                while self.queue.full():
                    print(f"{self.name} esta esperando que se libre un espacio en la cola para producir datos.")
                    self.cond.wait()
                obj = self.queue.put('objeto')
                print(f"{self.name} esta produciendo {obj}.")
                self.cond.notifyAll()