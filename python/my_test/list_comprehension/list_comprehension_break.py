def end_of_loop():
    raise StopIteration

stop_num = 4
def gen_n(n):
    print "n:",n
    return (n, n**n)
numbers = range(10)
even = list(end_of_loop() if n== stop_num else gen_n(n) for n in numbers if 0 == n %2)
# even = [end_of_loop() if n== 6 else n for n in numbers if 0 == n %2]
print even # [0, 2, 4]

import itertools
even_numbers = (gen_n(n) for n in numbers if not n % 2)
even1 = list(itertools.takewhile(lambda x: x[0] != stop_num, even_numbers))
print even1