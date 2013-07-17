# i first, j second
print [(i,j) for i in range(10) for j in range(11,20)]
print [(i,j) for i,j in zip(range(10), range(11,20)) if (i % 2 == 0)]

def get_some(some):
    print some
    return some

[(i,j) for i,j in zip(map(get_some, range(10)), range(11,20)) 
    if (i % 2 == 0)]
