from threading import Thread
from ejemplo2 import MyThread

if __name__ == "__main__":
    nameList = ["Thread1", "Thread2", "Thread3", "Thread4", "Thread5"]
    threadList = []
    for i in range(5):
        thread = MyThread(nameList[i])
        thread.start()
        threadList.append(thread)
    for thread in threadList:
        thread.join()
    print("\nAll threads have been terminated!\n")