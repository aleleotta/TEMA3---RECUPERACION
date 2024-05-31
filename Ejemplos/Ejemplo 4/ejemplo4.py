from threading import Thread, Condition
from random import randint
import time

class Cliente(Thread):
    libros = [False, False, False, False, False]
    cond = Condition()

    def __init__(self, name):
        Thread.__init__(self, name = name)

    def run(self):
        print(f"El cliente {self.name} entra en una libreria")
        pos = randint(0,4)
        print(f"El cliente {self.name} quiere coger el libro {pos}")
        Cliente.cond.acquire()
        while Cliente.libros[pos]: #Mientras sea True
            Cliente.cond.wait()
        Cliente.libros[pos] = True
        print(f"El cliente {self.name} tiene el libro {pos}")
        Cliente.cond.release()
        time.sleep(randint(1,5))
        Cliente.cond.acquire()
        Cliente.libros[pos] = False
        print(f"El cliente {self.name} deja de usar el libro {pos}")
        Cliente.cond.notifyAll()
        Cliente.cond.release()