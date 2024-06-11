from queue import Queue
from threading import Thread, Condition
import time
from productor import *
from consumidor import *

if __name__ == "__main__":
    listadoProductores = ["Productor1", "Productor2", "Productor3", "Productor4", "Productor5", "Productor6"]
    listadoConsumidores = ["Consumidor1", "Consumidor2", "Consumidor3", "Consumidor4", "Consumidor5", "Consumidor6"]
    cond = Condition()
    queue = Queue(2)
    for nombreProductor in listadoProductores:
        nuevoProductor = Productor(nombreProductor, cond, queue)
        nuevoProductor.start()
    for nombreConsumidor in listadoConsumidores:
        nuevoConsumidor = Consumidor(nombreConsumidor, cond, queue)
        nuevoConsumidor.start()