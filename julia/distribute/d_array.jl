p = println
arr = drand((100,100), workers()[1:4], [1,4])
p(arr.indexes)