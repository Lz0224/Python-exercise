import threading
import time

def wait_for_event(e):
    print 'wait_for_event : starting'
    e.wait()
    print 'wait_for_event : e.is_set()->', e.is_set()

def wait_for_event_timeout(e, t):
    print 'wait_for_event_timeout 666: starting'
    e.wait(t)           #人为添加阻塞函数（阻塞时间）
    print 'wait_for_event_timeout :6666 e.is_set()', e.is_set()

if __name__ == '__main__':
    e = threading.Event()
    w1 = threading.Thread(target = wait_for_event, args = (e,))
    w1.start()

    w2 = threading.Thread(target = wait_for_event_timeout, args = (e,2))
    w2.start()

    print 'main : waiting before calling Event.set()'
    time.sleep(4)
    e.set()
    print 'main : event is set'
