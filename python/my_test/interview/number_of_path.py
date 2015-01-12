def numberOfPaths (a):
    m = len(a)
    n = len(a[0])
    count = 0
    if a[0][0] == 0:
        return 0
    if n == 1 or m == 1:
        if all(flat(a)):
            return 1
    if a[0][1] == 1:
        count += numberOfPaths(getSubRect(a, 'col'))
    if a[1][0] == 1:
        count += numberOfPaths(getSubRect(a, 'row'))
    return count

def flat(l):
    return [item for sublist in l for item in sublist]

def getSubRect(a, sub_type='col'):
    m = len(a)
    n = len(a[0])
    if sub_type=='col':
        return [[a[i][j] for j in range(1, n) ] for i in range(m)]
    else:
        return a[1:]


if __name__ == '__main__':
    from minitest import *
    a0 = [ [1,1],
          [1,1]]
    a1 = [ [1,1,1],
           [0,1,1]]
    a2 = [ [1,1],
          [0,1],
          [0,1],
          [0,1],
          [0,1],
          [0,1],
          [0,1],
          [0,1],
          [1,1]]
    a3 = [ [1,1,1],
           [1,1,1], 
           [1,1,1], 
           [1,1,1]]
    a4 = [ [1,1,1,1],
           [1,1,1,1], 
           [1,1,1,1]]
    a5 = [ [0,1,1,1],
           [1,1,1,1], 
           [1,1,1,1]]

    with test(numberOfPaths):
       numberOfPaths(a0).must_equal(2)                 
       numberOfPaths(a1).must_equal(2)                 
       numberOfPaths(a2).must_equal(1)                 
       numberOfPaths(a3).must_equal(10)                 
       numberOfPaths(a4).must_equal(10)                 
       numberOfPaths(a5).must_equal(0)                 
    # with test(getSubRect):
    #     # getSubRect(a2,'row').pp()
    #     getSubRect(a1,'col').pp()
    # with test(flat):
    #     flat(a1).pp()