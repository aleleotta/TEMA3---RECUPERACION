from negocio import *

if __name__ == "__main__":
    listadoClientes = ["Cliente1", "Cliente2", "Cliente3", "Cliente4", "Cliente5", "Cliente6", "Cliente7", "Cliente8"]
    listadoHilos = []
    for nombreCliente in listadoClientes:
        nuevoCliente = Cliente(name = nombreCliente)
        nuevoCliente.start()
        listadoHilos.append(nuevoCliente)
    for hilo in listadoHilos:
        hilo.join()
    print("El hilo principal se ha terminado.")