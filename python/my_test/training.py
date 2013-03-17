lst = [1,2,3] # list
tup = (1,2,3) # tuple
dic = {1:"1", 2:"2"} # dictionary

print "list:",lst
print "tuple:",tup
print "dictionary:",dic



lst = [1,2,3]

def is_odd(x):
    return (x % 2)!=0

print filter(is_odd, lst)

lst = [1,2,3]
print filter(lambda x: (x%2)!=0, lst)
