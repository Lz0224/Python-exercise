a = 1

def out():
    b = 2
    def inner():
        nonlocal b
        global a
        a += 3
        b += 3
        print(a)
        print(b)
    inner()

out()
