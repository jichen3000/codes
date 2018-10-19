from multiprocessing import Process
from time import sleep

def f(n):
    print('in f')
    for i in range(n):
        print(i)
        sleep(0.5)

if __name__ == '__main__':
    p = Process(target=f, args=(10,))
    p.start()
    sleep(1)
    if p.is_alive():
        p.terminate()
    # p.join()