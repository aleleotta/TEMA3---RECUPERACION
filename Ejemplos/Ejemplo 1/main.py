from threading import Thread
from ejemplo1 import MyThread

if __name__ == "__main__":
    threadList = []
    for i in range (0, 100):
        thread = MyThread(i)
        thread.start()
        threadList.append(thread)
    for thread in threadList:
        thread.join()
    print("\nAll threads have been terminated!\n")