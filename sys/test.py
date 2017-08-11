from time import sleep
from greenlet import greenlet

def test1():
    sleep(1)
    print 1
    gr2.switch()
    print 2


def test2():
    sleep(1)
    print 'a'
    gr1.switch()
    print 'b'


gr1 = greenlet(test1)
gr2 = greenlet(test1)


gr1.switch()
gr2.switch()
