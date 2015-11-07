import threading
import time

def worker(index):
    """thread worker function"""
    print 'Worker {index}'.format(index=index)
    time.sleep(2)
    return

# threads = [ ]
threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()
print threads

print [threading.Thread(target=worker, args=(i,)).start() for i in range(5)]
