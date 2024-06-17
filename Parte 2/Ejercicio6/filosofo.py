from threading import Thread, Condition
from random import randint
import time

class Filosofo(Thread):

    cond = Condition()
    palillos = [False, False, False, False, False]

    def __init__(self, name):
        Thread.__init__(self, name = name)

    def run(self):
        while True:
            palilloLeft = int(self.name)
            palilloRight = (palilloLeft+1)%5
            print(f"Filosofo {self.name} se queda pensando.")
            time.sleep(randint(1,3))
            with Filosofo.cond:
                while Filosofo.palillos[palilloLeft] is True or Filosofo.palillos[palilloRight] is True:
                    print(f"Filosofo {self.name} se queda esperando.")
                    Filosofo.cond.wait()
                Filosofo.palillos[palilloLeft] = True
                Filosofo.palillos[palilloRight] = True
                print(f"Filosofo {self.name} esta comiendo.")
                time.sleep(randint(1,5))
                print(f"Filosofo {self.name} ha terminado de comer.")
                Filosofo.palillos[palilloLeft] = False
                Filosofo.palillos[palilloRight] = False
                Filosofo.cond.notifyAll()