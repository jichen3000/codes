
def ormap(fun, *iter):
    for i in zip(*iter):
        fun_result = fun(*i)
        if fun_result:
            return fun_result
    return False

import itertools
def ormap_list(fun, *iter):
    result_generator = (fun(*i) for i in zip(*iter))
    return (list(itertools.islice(itertools.dropwhile(lambda x: not x, result_generator),1))+[False,])[0]

def l2(i):
    # print i
    return i > 2

def l3(i,j):
    # print i,j
    return i > 2 and j > 2


if __name__ == '__main__':
    print ormap(l2, (1,2,3,4,5))
    print ormap(l2, (2,1,0))
    print ormap(l2, tuple()) 
    print ormap(l3, (2,3,4),(2,3,4))
    print ormap(l3, (2,1,0),(2,1,2))
    print ormap(l3, tuple(),tuple())
    print "other:"
    print ormap_list(l2, (1,2,3,4,5))
    print ormap_list(l2, (2,1,0))
    print ormap_list(l2, tuple()) 
    print ormap_list(l3, (2,3,4),(2,3,4))
    print ormap_list(l3, (2,1,0),(2,1,2))
    print ormap_list(l3, tuple(),tuple())

    print "timeit:"
    import timeit
    from functools import partial
    t_ormap = timeit.Timer(partial(ormap,l2, (1,2,3,4,5)))
    print "normal:",t_ormap.timeit()
    t_ormap_generator = timeit.Timer(partial(ormap,l2, (1,2,3,4,5)))
    print "t_ormap_generator:",t_ormap_generator.timeit()
    # print "generator:",timeit.timeit(stmt='ormap_list(l2, (1,2,3,4,5))',number=10000)


