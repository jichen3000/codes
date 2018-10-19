from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    p = Pool(2)
    print(p.map(f, range(10)))