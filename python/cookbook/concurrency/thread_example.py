import time
def countdown(n):
    while n > 0: 
        print('T-minus', n) 
        n -= 1 
        time.sleep(1)

from threading import Thread
import threading
import signal
# t = Thread(target=countdown, args=(5,)) 
# t.start()
# t.join()
# print "ok"

# threads = [Thread(target=countdown, args=(i,)) for i in range(3,5)]
# [t.start() for t in threads]
# [t.join() for t in threads]
# print "ok"

threading.get_ident()
aa = Thread(target=countdown, args=(30,))
aa.start()
aa.ident
signal.pthread_kill(aa.ident, 1)
aa.is_alive()
print("ok")