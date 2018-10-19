from multiprocessing import Process, Queue
from time import sleep

def producer(n, q):
    for i in range(n):
        q.put(i)
        sleep(1)
    q.put("end")
def consumer(q):
    v = q.get()
    v.p()
    while v != "end":
        v = q.get()
        # q.task_done()
        v.p()

if __name__ == '__main__':
    import print_helper
    q = Queue()
    p = Process(target=producer, args=(3,q))
    p.start()
    consumer(q)
    # sleep(3)
    # if p.is_alive():
    #     p.terminate()
    # p.join()