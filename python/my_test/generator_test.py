def firstn(n):
    num = 0
    print "firstn n:",n, num
    while num <= n:
        print "yield num:", num
        yield num
        num += 1

print sum(firstn(5))

print sum(firstn(5))

a = firstn(2)
print a.next()
print a.next()
# print a.next()
# print a.next()


a = firstn(5)
import operator
b = map(operator.itemgetter(), a)
print b