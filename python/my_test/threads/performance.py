def worker(n):
    for i in range(n):
        i * i

if __name__ == '__main__':
    from threading import Thread
    ts = [Thread(target=worker, args=(1000 * 1000 * 50,)) for _ in range(2)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    # from minitest import *

    # # with test(worker):
    # #     worker(1000 * 1000 * 30)
    # #     worker(1000 * 1000 * 30)

    # with test("for threads"):
    #     from threading import Thread
    #     ts = [Thread(target=worker, args=(1000 * 1000 * 30,)) for _ in range(2)]
    #     for t in ts:
    #         t.start()
    #     for t in ts:
    #         t.join()
