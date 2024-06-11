from random import randint
from threading import Thread, Semaphore
import time

class Cliente(Thread):
    carniceria = Semaphore(4)
    charcuteria = Semaphore(2)

    def __init__(self, name):
        Thread.__init__(self, name = name)

    def run(self):
        carnAtendido = False
        charAtendido = False
        while(not carnAtendido or not charAtendido):
            if(Cliente.carniceria._value > 0):
                Cliente.carniceria.acquire()
                print(f"{self.name} esta siendo atendido en la carniceria.")
                time.sleep(randint(1,5))
                print(f"{self.name} ha terminado de ser atendido en la carniceria y se marcha.")
                carnAtendido = True
                Cliente.carniceria.release()
            else:
                print(f"{self.name} esta esperando para ser atendido en la carniceria.")

            if(Cliente.carniceria._value > 0):
                Cliente.charcuteria.acquire()
                print(f"{self.name} esta siendo atendido en la charcuteria.")
                time.sleep(randint(1,5))
                print(f"{self.name} ha terminado de ser atendido en la charcuteria y se marcha.")
                charAtendido = True
                Cliente.charcuteria.release()
            else:
                print(f"{self.name} esta esperando para ser atendido en la charcuteria.")
        print(f"{self.name} se marcha del negocio.")