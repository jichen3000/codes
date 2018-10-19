from multiprocessing import Process, Queue

def handle(process_id, shared_queue):
    a = shared_queue.get()
    print("process {}, value {}".format(process_id, a))


def main():
    shared_queue = Queue()
    for i in range(10):
        shared_queue.put(i)
    thread_count = 2
    all_processes = []
    for i in range(thread_count):
        cur = Process(target=handle, args=(i, shared_queue))
        cur.start()
        all_processes.append(cur)
    for cur in all_processes:
        cur.join()

main()