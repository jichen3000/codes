def firstn(n):
    num = 0
    print "firstn n:",n, num
    while num <= n:
        print "yield num:", num
        yield num
        num += 1

print sum(firstn(5))

print sum(firstn(5))