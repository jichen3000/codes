from itertools import *

def genf(x):
	print "genf x:",x
	return (x,x*x)

generator_list = (genf(i) for i in range(9))
# print list(islice(generator_list, 3))
print list(islice(dropwhile(lambda x: x[0]!=3, generator_list),1))
# print islice(generator_list, 3)
# print list(islice(generator_list, 1))
# print list(islice(count(10),5))