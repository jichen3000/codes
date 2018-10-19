from multiprocessing import Pool

def worker(n):
    for i in range(n):
        i * i

if __name__ == '__main__':
    count = 1000 * 1000 * 50
    # worker(count)
    # worker(count)
    p = Pool(5)
    print(p.map(worker, [count,count]))