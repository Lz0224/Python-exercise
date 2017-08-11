import multiprocessing
from time import sleep
import os

def worker(sec):
    print "parent PID:", os.getppid()
    while 1:
        sleep(sec)
        print "worker...."
    print os.getpid()
    return


if __name__ == "__main__":
    print os.getppid()
    p = multiprocessing.Process(target = worker, name = "work1", args = (3,))
    p.start()
    print os.getpid()
