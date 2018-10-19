def get_absolute_p(n, k):
    if k == 0:
        return range(1,n+1)
    if n % 2 == 0 and (n/2) % k == 0:
        the_p = [0 for i in xrange(n)]
        for i in xrange(0,n):
            if the_p[i] == 0:
                the_p[i] = i+1+k
                the_p[i+k] = i+1
        return the_p
    return [-1]


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = map(int, raw_input().strip().split(' '))
    for i in get_absolute_p(n, k):
        print(i),
    print("")

# if __name__ == '__main__':
#     from minitest import *

#     with test(get_absolute_p):
#         get_absolute_p(10, 1).must_equal([2, 1, 4, 3, 6, 5, 8, 7, 10, 9])
#         get_absolute_p(10, 3).must_equal([-1])
#         get_absolute_p(8, 2).must_equal([3, 4, 1, 2, 7, 8, 5, 6])