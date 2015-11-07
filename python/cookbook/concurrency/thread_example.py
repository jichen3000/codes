import time
def countdown(n):
    while n > 0: 
        print('T-minus', n) 
        n -= 1 
        time.sleep(1)

from threading import Thread

# t = Thread(target=countdown, args=(5,)) 
# t.start()
# t.join()
# print "ok"

threads = [Thread(target=countdown, args=(i,)) for i in range(3,5)]
[t.start() for t in threads]
[t.join() for t in threads]
print "ok"