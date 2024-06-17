from filosofo import Filosofo

if __name__ == "__main__":
    for i in range(5):
        filosofo = Filosofo(str(i))
        filosofo.start()