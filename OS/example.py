import threading
from time import sleep

data = 0

#防止两个进程临界争夺资源，用进程锁将全局变量锁住，就是将在一个线程使用全局变量时，I/O将其阻塞，使用完之后在打开。。。。
def a(e):
    # e.wait()
    # e.clear()
    global data   #提示在函数内使用全局变量。
    data = 10
    sleep(0.5)
    print "process a :", data
    # e.set()

def b(e):
    # e.wait()
    # e.clear()
    global data
    data = 100
    print "process b :", data
    # e.set()

if __name__ == '__main__':    #相当于while循环
    e = threading.Event()    #产生一个

    w1 = threading.Thread(target = a, args = (e,))   #产生一个线程
    w1.start()      #开始运行一个线程

    w2 = threading.Thread(target = b, args = (e,))
    w2.start()

    print 'main : waiting before calling Event.set()'
    sleep(2)
    print 'over'
