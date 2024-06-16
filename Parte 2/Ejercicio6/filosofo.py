from threading import Thread, Condition
from random import randint
import time

class Filosofo(Thread):

    def __init__(self, name, cond: Condition):
        Thread.__init__(name = name)
        self.cond = cond

    def run(self):
        pass