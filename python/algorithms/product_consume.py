from Queue import Queue

queue = Queue()
def product(item):
    queue.put(item)

def consume():
    return queue.get()
