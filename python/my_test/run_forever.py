import time

def do_some (i):
    time.sleep(i)
    print i

[do_some(i) for i in range(10)]
