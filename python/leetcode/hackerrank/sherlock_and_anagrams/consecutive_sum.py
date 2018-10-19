def consecutive(num):
    limit = num // 2 + 1
    res = 0
    for s in range(1, limit):
        for n in range(2, limit):
            if (2*s+n-1) * n == 2 * num:
                res += 1
                break
    return res

def consecutive(num):
    res = 0
    n = 3
    while 2 * num >= n * (n+1):
        if num % n == 0:
            # print(n)
            res += 1
        n += 2
    n = 2
    while 2 * num >= n * (n+1):
        if (num - n/2) % n == 0: 
            # print(n)
            res += 1
        n += 2
    return res

# def consecutive(num):
#     res = 0
#     l = 1
#     while 2 * num > l * (l+1):
#         if (num-l*(l+1)//2) % (l+1) == 0:
#         # a = (num-l*(l+1)//2) / (l+1)
#         # if a == int(a):
#             # print(n)
#             res += 1
#         l += 1
#     return res

if __name__ == '__main__':
    from minitest import *

    with test(consecutive):
        consecutive(15).must_equal(3)
        consecutive(10000000).must_equal(7)
        consecutive(100000000000).must_equal(11)