def fib(n):
    if n <= 1:
        return n
    pre2 = pre1 = cur = 1
    for i in xrange(2,n):
        cur = pre2 + pre1
        pre2, pre1 = pre1, cur
    return cur

if __name__ == '__main__':
    from minitest import *

    with test(fib):
        for i in range(10):
            fib(i).p()